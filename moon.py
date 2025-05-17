import geocoder
import pylunar
import datetime
from utils import convert_days_to_dhm


def decimal_to_dms(degree):
    is_positive = degree >= 0
    degree = abs(degree)
    d = int(degree)
    m = int((degree - d) * 60)
    s = (degree - d - m / 60) * 3600
    if not is_positive:
        d = -d
    return (int(d), int(m), int(s))

# Step 1: Get current location
location = geocoder.ip('me')
latitude, longitude = location.latlng

# Step 2: Convert to DMS
lat_dms = decimal_to_dms(latitude)
lon_dms = decimal_to_dms(longitude)
print(lat_dms, lon_dms)

# Step 3: Set up the observer with pylunar
moon_info = pylunar.MoonInfo(lat_dms, lon_dms)  # Name, lat, lon, elevation
#moon_info = pylunar.MoonInfo((52, 22, 26.508), (4, 53, 22.884))
moon_info.update(datetime.datetime.utcnow())

# Step 4: Get the current moon phase
phase_name = moon_info.phase_name()
phase_percentage = moon_info.fractional_phase()
moon_emoji = moon_info.phase_emoji()
print(moon_info.time_to_full_moon())
d, h, m = convert_days_to_dhm(moon_info.time_to_full_moon())
print(f"Time until next full moon: {d} days, {h} hours, {m} minutes")


print(f"Current Moon Phase: {phase_name}")
