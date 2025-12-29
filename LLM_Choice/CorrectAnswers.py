"""
Software Lab 2025 Group 25

File made by: Eduardo Silva (03805057)
eduardo.silva@tum.de

Description: 

This file is responsible for using the Agent's tools from its raw implementation. 
With these tools, it is possible to use the user's queries defined in the ChooseLLM.ipynb file, 
such that we get the correct expected answers. 

The correct answers are saved into a .json file that is later used to evaluate both systems on performance.

"""



import joblib


material_hardness = {'N': 70, 'P': 180, 'K': 160}

def get_wear(material: str, feed: float, cutting_speed: float) -> str:
    """
    This tool allows for the calculation of wear of a drill bit. 

    Inputs: 
        - material: letter representation of material being drilled.
        - feed: value for feed rate when drilling in [mm/min] units.
        - cutting_speed: value for cutting speed when drilling in [m/min] units.

    Output: Probabilities of Failure Criteria
    """
    
    hardness = material_hardness[material]
    regressor = joblib.load(f"saved_models/regressor_{material}.pkl")
    classifier = joblib.load(f"saved_models/classifier_{material}.pkl")
    scaler = joblib.load(f"saved_models/scaler_{material}.pkl")


    torque_pred = regressor.predict([[hardness, feed]])[0]
    input_scaled = scaler.transform([[cutting_speed, torque_pred, feed]])
    probs = classifier.predict_proba(input_scaled)[0]

    return (f'[{probs[0]*100:.1f}, {probs[1]*100:.1f}, {probs[2]*100:.1f}]')

def get_quality(cooling: float, cutting_speed: float, feed: float, drill_bit_material = None) -> str:

    """
    This tool allows for quality evaluation of drilling.

    Inputs: 
        - cooling: float representing the amount of cooling while drilling in [%] units
        - feed: value for feed rate when drilling in [mm/min] units.
        - cutting_speed: value for cutting speed when drilling in [m/min] units
        - drill_bit_material: represents the material of the drill bit, if no value is provided use "None".

    Output: Good or Bad Quality.
    """

    # for BEF Criteria
    if cooling <= 12.50 and cutting_speed <= 22.01:
        
        if (feed <= 0.19 and feed > 0.14) or feed <= 0.14:
            BEF = 'Bad'
        
        elif feed >= 0.19 and cutting_speed <= 16.70:
            BEF = 'Bad'

    else: BEF = 'Good'


    # for CCF Criteria
    if cooling <= 37.50 and feed > 124.50:
        CCF = 'Bad'

    elif cooling > 37.50 and feed > 205.50 and \
        (drill_bit_material == "H" or drill_bit_material == "N"):
        CCF = 'Bad'

    elif cooling <= 37.50 and feed <= 124.50 and drill_bit_material == "W":
        CCF = 'Bad'

    else: CCF = 'Good'

    return f'[{BEF}, {CCF}]'


CorrectAnswersALL = {
    "EASY": [
    get_wear('P', 0.2, 100.0),
    get_quality(12.5, 16.7, 0.13),
    get_wear('N', 0.3, 120.0)
    ],

    "MEDIUM": [
        get_wear('K', 0.25, 100.0),
        get_quality(10.5, 254.0, 5.08),
        get_quality(15.0, 75.0, 0.15),
        get_wear('P', 0.2, 100.0),
    ],

    "HARD": [
        [get_wear('P', 0.3, 120.0), get_quality(12.5, 120.0, 0.3, 'N')],
        [get_wear('K', 0.25, 100.0), get_quality(10.0, 100.0, 0.25)],
        [get_wear('N', 0.2, 80.0), get_quality(10.0, 80.0, 0.2, 'H')]
    ]
}

CorrectAnswers = {
    "EASY": [
    get_wear('P', 0.2, 100.0),
    get_quality(12.5, 16.7, 0.13),
    get_wear('N', 0.3, 120.0)
    ],

    "MEDIUM": [
        get_wear('K', 0.25, 100.0),
        get_quality(10.5, 254.0, 5.08),
        get_quality(15.0, 75.0, 0.15),
        get_wear('P', 0.2, 100.0),
    ],
}

import json

with open("correct_answers_ALL.json", "w") as f:
    json.dump(CorrectAnswersALL, f, indent=4)

with open("correct_answers_EASY_MEDIUM.json", "w") as f:
    json.dump(CorrectAnswers, f, indent=4)

