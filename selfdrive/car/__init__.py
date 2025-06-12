# 在imports中添加  
from selfdrive.car.virtual.interface import CarInterface as VirtualInterface  
from selfdrive.car.virtual.values import CAR as VIRTUAL  
  
# 在interfaces字典中添加  
interfaces = {  
    # ... 现有接口  
    VIRTUAL.VIRTUAL: VirtualInterface,  
}
