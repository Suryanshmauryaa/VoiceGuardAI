import smtplib
from email.mime.text import MIMEText

def trigger_alerts(speaker, emotion, threat):
    msg = MIMEText(f"🚨 Threat Detected!\nSpeaker: {speaker}\nEmotion: {emotion}\nThreat Word: {threat}")
    msg["Subject"] = "VoiceGuard AI+ - Security Alert"
    msg["From"] = "suryanshmofficial@gmail.com"
    msg["To"] = "suryansh.bizz@gmail.com"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("suryanshmofficial@gmail.com", "gxvv plqk orkl cwnk")
        server.send_message(msg)
