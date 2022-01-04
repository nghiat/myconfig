import json
import os

def setup():
    if os.name == "nt":
        config_dir = "~/AppData/Roaming/calibre"
    else:
        config_dir = "~/.config/calibre"
    config_dir = os.path.expanduser(config_dir)
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)
    with open("viewer-webengine.json", "r", encoding="utf-8") as f:
        predefined_config = json.load(f)
    viewer_webengine_path = os.path.join(config_dir, "viewer-webengine.json")
    data = {}
    if os.path.exists(viewer_webengine_path):
        with open(viewer_webengine_path, 'r', encoding="utf-8") as f:
            data = json.load(f)
    data.update(predefined_config)
    with open(viewer_webengine_path, 'w+', encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
