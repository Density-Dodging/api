import json
with open('config.json') as config_file:
    config = json.load(config_file)

class Config:
    def get(property):
        return config[property]

def log(tag, message):
    if (Config.get("environment") == "dev"):
        print(f"[{tag}] {message}")
