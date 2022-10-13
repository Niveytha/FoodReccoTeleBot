from datetime import datetime

def handle_responses(inputText):
    userMessage = str(inputText).lower()

    if userMessage in ("hello", "hi", "sup"):
        return "Hey! How's it going?"

    if userMessage in ("who are you", "who are you?", "who r u", "who r you", "who are u"):
        return "I am your first ever bot!"    

    if userMessage in ("time", "time?"):
        now = datetime.now()
        dateTime = now.strftime("%d/%m/%y, %H:%M:%S")
        return dateTime

    return "bro what you sayin"