#!/usr/bin/env python3
#!/usr/bin/env python3
#======================================================================#
# Module:      NGV_P_Basic_5_spawnvehicle.py
# Description: Practice code for spawning a vehicle
#
# Authors: Seokhwan Jeong (shjeong00@hanyang.ac.kr)
#
# Revision History
#      Feb  17, 2026: Seokhwan Jeong - Created.
#      Feb  22, 2026: Seokhwan Jeong - Made Empty Template for Student Exercise
#======================================================================#
import carla

# ============================================================
# Client를 CARLA 시뮬레이터에 연결
# ============================================================
client = carla.Client('localhost', 2000)
client.set_timeout(5.0)
world = client.get_world()

original_settings = world.get_settings()

# ============================================================
# Synchronous 모드 설정
# ============================================================
settings = world.get_settings()
settings.synchronous_mode = True
settings.fixed_delta_seconds = 0.05
world.apply_settings(settings)

# ============================================================
# Traffic Manager를 연결
# ============================================================
traffic_manager = client.get_trafficmanager(8000)
traffic_manager.set_synchronous_mode(True)
tm_port = traffic_manager.get_port()

# ============================================================
# Ego 차량 Spawn하기
# ============================================================
#-[TODO]- Get the blueprint of the ego vehicle
ego_bp = 
#-[TODO]- Set the attribute of the ego vehicle
ego_bp.set_attribute

#-[TODO]- Get the spawn points of the map
spawn_points = 

try:
    #-[TODO]- Select the Spawnpoint and spawn the ego vehicle
    ego_transform = 
    ego_vehicle = 
    #-[TODO]- Set the ego vehicle to autopilot

    while True:
        world.tick()

except KeyboardInterrupt:
    print("\n[Ctrl+C] Destroying vehicle...")
    #-[TODO]-Destroy ego vehicle

finally:
    try:
        world.apply_settings(original_settings)
    except Exception:
        pass