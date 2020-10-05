import os
import xml.etree.ElementTree as ET

# Light theme is based on old https://cs.chromium.org/ theme.
# Dark theme is based on visual studio dark theme.
colors256 = {
    # Light
    "tLB": "15", "LB": "#ffffff",
    "tLF": "0", "LF": "#000000",
    "tLCommentF": "1", "LCommentF": "#800000",
    "tLStringF": "2", "LStringF": "#008000",
    "tLKeywordF": "4", "LKeywordF": "#0000ff",
    "tLSelectionB": "33", "LSelectionB": "#0087ff",
    "tLSearchB": "121", "LSearchB": "#87ffaf",
    "tLMatchBracketB": "121", "LMatchBracketB": "#87ffaf",
    "tLCurrentLineB": "254", "LCurrentLineB": "#e4e4e4",
    "tLMaxColumnB": "254", "LMaxColumnB": "#e4e4e4",
    "tLCompletePopupB": "254", "LCompletePopupB": "#e4e4e4",
    "tLCompletePopupF": "0", "LCompletePopupF": "#000000",
    "tLSpecialKeyF": "254", "LSpecialKeyF": "#e4e4e4",
    # Dark
    "tDB": "234", "DB": "#1c1c1c",
    "tDF": "253", "DF": "#dadada",
    "tDCommentF": "71", "DCommentF": "#5faf5f",
    "tDStringF": "174", "DStringF": "#d78787",
    "tDKeywordF": "183", "DKeywordF": "#d7afff",
    "tDSelectionB": "24", "DSelectionB": "#005f87",
    "tDSearchB": "241", "DSearchB": "#626262",
    "tDMatchBracketB": "25", "DMatchBracketB": "#005faf",
    "tDCurrentLineB": "238", "DCurrentLineB": "#444444",
    "tDMaxColumnB": "238", "DMaxColumnB": "#444444",
    "tDCompletePopupB": "238", "DCompletePopupB": "#444444",
    "tDCompletePopupF": "253", "DCompletePopupF": "#dadada",
    "tDSpecialKeyF": "240", "DSpecialKeyF": "#585858",

    # Terminal usually uses color name Black, White, etc.
    "LBlack": "#000000",
    "LWhite": "#ffffff",
    "LRed": "#800000",
    "LGreen": "#008000",
    "LBlue": "#0000ff",
    "LYellow": "#808000",
    "LMagenta": "#800080",
    "LCyan": "#008080",

    "DBlack": "#1c1c1c",
    "DWhite": "#dadada",
    "DRed": "#d78787",
    "DGreen": "#5faf5f",
    "DBlue": "#005faf",
    "DYellow": "#fdfbac",
    "DMagenta": "#68217a",
    "DCyan": "#9affff",
}


def generate_from_template_files(templates_map):
    for template_file, output_file in templates_map.items():
        output_str = ""
        expanded_output = os.path.expanduser(output_file)
        with open(template_file) as f:
            output_str = f.read().format(**colors256)
        with open(expanded_output, "w") as f:
            f.write(output_str)
        print("Generated {0} from {1} with colors code replaced"
              .format(expanded_output, template_file))


def delete_generated_files(templates_map):
    for template_file, output_file in templates_map.items():
        expanded_output = os.path.expanduser(output_file)
        if os.path.exists(expanded_output):
            os.remove(expanded_output)
            print("Deleted file {0} that was generated from {1}"
                  .format(expanded_output, template_file))


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
