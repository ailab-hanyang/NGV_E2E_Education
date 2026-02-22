#!/usr/bin/env python3
#======================================================================#
# Module:      NGV_P_Basic_1_connectserver.py
# Description: Connect to CARLA server and get world information
#
# Authors: Seokhwan Jeong (shjeong00@hanyang.ac.kr)
#
# Revision History
#      Feb  13, 2026: Seokhwan Jeong - Created.
#      Feb  22, 2026: Seokhwan Jeong - Made Empty Template for Student Exercise
#======================================================================#
#-[TODO]- Import CARLA Library

# ============================================================
# Client를 CARLA 시뮬레이터에 연결
# ============================================================
#-[TODO]- Connect to CARLA server using carla.Client and set timeout


# ============================================================
# Server에서 정보 읽어오기
# ============================================================
#-[TODO]- Get information from the server using get_..() functions
world = 
weather = 
blueprint_library = 
spectator = 

# ============================================================
# Spectator 위치 변경하기
# ============================================================
#-[TODO]- Use carla.Location & .Rotation to set the spectator's position and orientation
transform = carla.Location(x=???, y=???, z=???)
rotation = carla.Rotation(roll=???, pitch=???, yaw=???)
#-[TODO]- Set the spectator's transform using set_transform() function
spectator.
