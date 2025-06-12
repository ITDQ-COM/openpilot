from opendbc.car import CarSpecs, PlatformConfig, dbc_dict  
from opendbc.car.structs import CarParams  
  
class CAR:  
    VIRTUAL = "VIRTUAL"  
  
PLATFORM_CONFIGS = {  
    CAR.VIRTUAL: PlatformConfig(  
        [CarSpecs(mass=1500, wheelbase=2.7, steerRatio=15.0)],  
        dbc_dict('virtual', None)  
    ),  
}
