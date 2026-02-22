#!/usr/bin/env python3
#======================================================================#
# Module:      NGV_Basic_4_weatherchanger.py
# Description: Connect to CARLA server and change the weather
#
# Authors: Seokhwan Jeong (shjeong00@hanyang.ac.kr)
#
# Revision History
#      Feb  16, 2026: Seokhwan Jeong - Created.
#======================================================================#
import carla

# ============================================================
# Client를 CARLA 시뮬레이터에 연결
# ============================================================
client = carla.Client('localhost', 2000)
client.set_timeout(5.0)

# ============================================================
# Server에서 정보 읽어오기
# ============================================================
world = client.get_world()

# ============================================================
# 날씨 설정하기
# ============================================================
#-[TODO]- Get current weather using get_weather() function
weather = 

#-[TODO]- Set weather parameters (ex: cloudiness, precipitation, precipitation_deposits, wetness, sun_altitude_angle, sun_azimuth_angle)
weather.

#-[TODO]- Set weather configuration using set_weather() function
world.