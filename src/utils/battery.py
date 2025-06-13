def get_battery_level():
    import psutil
    battery = psutil.sensors_battery()
    return battery.percent if battery else None

def check_battery_level():
    level = get_battery_level()
    if level is not None:
        return level > 75
    return False