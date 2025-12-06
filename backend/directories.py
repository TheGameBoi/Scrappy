import json
from pathlib import Path

# Pathlib directory for the root, image, json, and css files.
main_dir = Path(__file__).parent.resolve()
img_dir = main_dir / "imgs"
json_path = main_dir / "jsons" / "items.json"
css_path = main_dir / "themes" / "mode.css"
icon_file = ["recycler.ico", "help.ico", "info.ico", "scrappy.ico", "x.png", "github.png"]
icon_path = {name: img_dir / name for name in icon_file}


# JSON function to read the JSON data.
def load_from_json(file_path):
    with open(file_path, 'r') as my_json:
        data = json.load(my_json)
        return data
