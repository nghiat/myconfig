import xml.etree.ElementTree as ET
from scripts.colors import colors256

links = {
    "~/Library/ApplicationSupport/iTerm2/Scripts/AutoLaunch/switch_color.py": "switch_color.py",
}

note = '''sudo pmset -a disablesleep 0'''


def generate_preset(colors, filename):
    root = ET.Element("plist")
    root.set("version", "1.0")
    root_dict = ET.SubElement(root, "dict")
    for text, color in colors.items():
        ET.SubElement(root_dict, "key").text = text
        dict = ET.SubElement(root_dict, "dict")
        color = colors256[color]
        ET.SubElement(dict, "key").text = "Alpha Component"
        ET.SubElement(dict, "real").text = "1"
        ET.SubElement(dict, "key").text = "Red Component"
        ET.SubElement(dict, "real").text = str(int(color[1: 3], 16) / 255.0)
        ET.SubElement(dict, "key").text = "Green Component"
        ET.SubElement(dict, "real").text = str(int(color[3: 5], 16) / 255.0)
        ET.SubElement(dict, "key").text = "Blue Component"
        ET.SubElement(dict, "real").text = str(int(color[5: 7], 16) / 255.0)
        ET.SubElement(dict, "key").text = "Color Space"
        ET.SubElement(dict, "string").text = "sRGB"
    doctype = '<?xml version="1.0" encoding="UTF-8"?>\n'\
              '<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">'
    with open(filename, "w") as f:
        f.write(doctype)
        f.write(ET.tostring(root, encoding="unicode"))


def generate_iterm2_presets():
    shared = {
        "Ansi 0 Color": "Black",
        "Ansi 1 Color": "Red",
        "Ansi 2 Color": "Green",
        "Ansi 3 Color": "Yellow",
        "Ansi 4 Color": "Blue",
        "Ansi 5 Color": "Magenta",
        "Ansi 6 Color": "Cyan",
        "Ansi 7 Color": "White",
        "Ansi 8 Color": "Black",
        "Ansi 9 Color": "Red",
        "Ansi 10 Color": "Green",
        "Ansi 11 Color": "Yellow",
        "Ansi 12 Color": "Blue",
        "Ansi 13 Color": "Magenta",
        "Ansi 14 Color": "Cyan",
        "Ansi 15 Color": "White",
        "Selection Color": "Yellow",
    }
    light = {
        "Background Color": "White",
        "Bold Color": "Black",
        "Cursor Color": "Black",
        "Cursor Text Color": "White",
        "Foreground Color": "Black",
        "Selected Text Color": "White",
    }
    dark = {
        "Background Color": "Black",
        "Bold Color": "White",
        "Cursor Color": "White",
        "Cursor Text Color": "Black",
        "Foreground Color": "White",
        "Selected Text Color": "Black",
    }
    light.update(shared)
    dark.update(shared)
    generate_preset(light, "ez.itermcolors")
    generate_preset(dark, "ez_dark.itermcolors")



def setup():
    generate_iterm2_presets()
