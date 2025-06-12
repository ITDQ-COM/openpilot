#!/bin/bash  
export NOBOARD=1  
export SIMULATION=1  
export PASSIVE=1  
  
# 设置虚拟车辆参数  
echo -n "VIRTUAL" > /data/params/d/CarFingerprint  
echo -n "1" > /data/params/d/IsLdwEnabled  
  
# 启动openpilot  
cd /data/openpilot  
./launch_chffrplus.sh
