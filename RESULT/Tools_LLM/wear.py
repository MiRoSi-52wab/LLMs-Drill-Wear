from langchain_core.tools import tool
import joblib


material_hardness = {'N': 70, 'P': 180, 'K': 160}

@tool
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

    return (f"Probabilities -> Safe: {probs[0]*100:.1f}%, Warning: {probs[1]*100:.1f}%, Fail: {probs[2]*100:.1f}%")


