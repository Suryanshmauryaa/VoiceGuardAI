import re

def detect_threat(transcript):
    threat_keywords = ["bomb", "kill", "attack", "shoot", "explode", "terrorist"]
    
    if transcript:
        for keyword in threat_keywords:
            if re.search(rf'\b{keyword}\b', transcript.lower()):
                return f"Threat Detected: {keyword}"
    return "No Threat"
