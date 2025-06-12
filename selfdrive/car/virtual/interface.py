import math  
from cereal import car, messaging  
from openpilot.common.params import Params  
from openpilot.common.realtime import DT_CTRL  
from opendbc.car import CarSpecs, PlatformConfig  
from opendbc.car.interfaces import CarInterfaceBase  
  
class CarInterface(CarInterfaceBase):  
    def __init__(self, CP, CarController, CarState):  
        super().__init__(CP, CarController, CarState)  
        self.params = Params()  
        self.sm = messaging.SubMaster(['gpsLocationExternal'])  
          
    @staticmethod  
    def _get_params(ret, candidate, fingerprint, car_fw, experimental_long, docs):  
        ret.carName = "virtual"  
        ret.safetyConfigs = [car.CarParams.SafetyConfig(safetyModel=car.CarParams.SafetyModel.noOutput)]  
        ret.dashcamOnly = True  
        ret.passive = True  
        ret.notCar = True  
        return ret  
  
    def _update(self, c):  
        ret = car.CarState.new_message()  
          
        # 从GPS获取速度  
        self.sm.update(0)  
        if self.sm.valid['gpsLocationExternal']:  
            gps_data = self.sm['gpsLocationExternal']  
            ret.vEgo = gps_data.speed  # GPS速度 (m/s)  
        else:  
            ret.vEgo = 0.0  
              
        # 固定转向角为0度  
        ret.steeringAngleDeg = 0.0  
        ret.steeringRateDeg = 0.0  
          
        # 其他必要的车辆状态  
        ret.gearShifter = car.CarState.GearShifter.drive  
        ret.doorOpen = False  
        ret.seatbeltUnlatched = False  
        ret.canValid = True  
        ret.standstill = ret.vEgo < 0.1  
          
        return ret  
  
    def apply(self, c, now_nanos):  
        # 不发送任何控制指令  
        return car.CarControl.Actuators.new_message(), []
