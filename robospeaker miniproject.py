import os         # os module in Python is used to interact with the operating system.


while True:
    text = input("Enter what you want to speak through robospeaker (type 'stop' to exit): ")
    
    if text == "stop":
        print("Robo Speaker stopped")
        break
    
    # Windows Text-to-Speech using PowerShell
    os.system(f'powershell -Command "Add-Type –AssemblyName System.speech; $speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; $speak.Speak(\'{text}\');"')
