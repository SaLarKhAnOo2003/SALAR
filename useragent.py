import random

apps = [
    "com.facebook.katana",
    "com.facebook.lite",
    "com.facebook.orca",
    "com.facebook.adsmanager"
]

android_versions = ["10", "11", "12", "13", "14"]

devices = [
    "SM-G991B","SM-A205F","SM-A105F",
    "Redmi Note 8","Redmi 9A",
    "TECNO LH7n","Infinix X688B"
]

def ua1():
    android = random.choice(android_versions)
    device = random.choice(devices)
    app = random.choice(apps)

    return f"Dalvik/2.1.0 (Linux; U; Android {android}; {device}) [{app}]"
