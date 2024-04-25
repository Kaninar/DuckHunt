import json

with open("settings.json") as file:
    data = json.load(file)
    SCREEN_WIDTH, SCREEN_HEIGHT = data["current_screen_size"]["width"], data["current_screen_size"]["height"]
    FRAMERATE = data["framerate"]
