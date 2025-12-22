from langchain_core.tools import tool
from typing import Optional

@tool
def get_quality(cooling: float, cutting_speed: float, feed: float, drill_bit_material: Optional[str] = None) -> str:

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

    return (f"For these parameters, it is possible to say that:\nThere will be {BEF} Edge Quality and {CCF} Compression Chips Quality.")