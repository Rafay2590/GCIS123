def get_normal_range(device_name):
    """Takes a device name, cleans up the text, and returns its normal min and max energy range."""
    name = device_name.strip().title()
    if name == "Led Light":
        return 0.01, 0.10
    elif name == "Television":
        return 0.05, 0.50
    elif name == "Refrigerator":
        return 0.10, 1.50
    elif name == "Washing Machine":
        return 0.30, 2.50
    elif name == "Air Conditioner":
        return 0.50, 5.00
    else:
        return None, None

def get_energy_status(device_name, energy):
    """Compares a device's energy reading against its normal range to return Normal, High, or Critical."""
    low, high = get_normal_range(device_name)
    if low is None:
        return "Unknown"
    if energy < 0:
        return "Invalid"
    if energy >= low and energy <= high:
        return "Normal"
    elif energy <= high * 1.5:
        return "High"
    else:
        return "Critical"

def requires_attention(status):
    """Checks the status and returns True if the device needs attention, otherwise False."""
    if status == "High" or status == "Critical":
        return True
    else:
        return False

def calculate_cost(energy, rate):
    """Calculates total electricity cost by multiplying energy by the rate and rounds it to two decimals."""
    if energy < 0:
        return 0.0
    cost = energy * rate
    return round(cost, 2)

def get_feedback(device_name, status, energy):
    """Provides smart troubleshooting advice based on the device name, status, and energy usage."""
    name = device_name.strip().title()
    if status == "Normal":
        return "Device is working fine."
    elif status == "High":
        if name == "Air Conditioner":
            return "Check your AC temperature settings."
        else:
            return "Energy usage is higher than normal."
    elif status == "Critical":
        return "Danger! Check this device immediately."
    else:
        return "Error with device name or energy."
