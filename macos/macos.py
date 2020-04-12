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
    light = {
        "Background Color": "LWhite",
        "Bold Color": "LBlack",
        "Cursor Color": "LBlack",
        "Cursor Text Color": "LWhite",
        "Foreground Color": "LBlack",
        "Selected Text Color": "LWhite",

        "Ansi 0 Color": "LBlack",
        "Ansi 1 Color": "LRed",
        "Ansi 2 Color": "LGreen",
        "Ansi 3 Color": "LYellow",
        "Ansi 4 Color": "LBlue",
        "Ansi 5 Color": "LMagenta",
        "Ansi 6 Color": "LCyan",
        "Ansi 7 Color": "LWhite",
        "Ansi 8 Color": "LBlack",
        "Ansi 9 Color": "LRed",
        "Ansi 10 Color": "LGreen",
        "Ansi 11 Color": "LYellow",
        "Ansi 12 Color": "LBlue",
        "Ansi 13 Color": "LMagenta",
        "Ansi 14 Color": "LCyan",
        "Ansi 15 Color": "LWhite",
        "Selection Color": "LYellow",
    }
    dark = {
        "Background Color": "DBlack",
        "Bold Color": "DWhite",
        "Cursor Color": "DWhite",
        "Cursor Text Color": "DBlack",
        "Foreground Color": "DWhite",
        "Selected Text Color": "DBlack",

        "Ansi 0 Color": "DBlack",
        "Ansi 1 Color": "DRed",
        "Ansi 2 Color": "DGreen",
        "Ansi 3 Color": "DYellow",
        "Ansi 4 Color": "DBlue",
        "Ansi 5 Color": "DMagenta",
        "Ansi 6 Color": "DCyan",
        "Ansi 7 Color": "DWhite",
        "Ansi 8 Color": "DBlack",
        "Ansi 9 Color": "DRed",
        "Ansi 10 Color": "DGreen",
        "Ansi 11 Color": "DYellow",
        "Ansi 12 Color": "DBlue",
        "Ansi 13 Color": "DMagenta",
        "Ansi 14 Color": "DCyan",
        "Ansi 15 Color": "DWhite",
        "Selection Color": "DYellow",
    }
    generate_preset(light, "ez.itermcolors")
    generate_preset(dark, "ez_dark.itermcolors")



def setup():
    generate_iterm2_presets()
