import os

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
    # "tLSelectionF": "15", "LSelectionF": "#ffffff",
    "tLSearchB": "121", "LSearchB": "#87ffaf",
    "tLMatchBracketB": "121", "LMatchBracketB": "#87ffaf",
    "tLCurrentLineB": "254", "LCurrentLineB": "#e4e4e4",
    "tLMaxColumnB": "254", "LMaxColumnB": "#e4e4e4",
    "tLCompletePopupB": "254", "LCompletePopupB": "#e4e4e4",
    "tLCompletePopupF": "0", "LCompletePopupF": "#000000",
    # Dark
    "tDB": "234", "DB": "#1c1c1c",
    "tDF": "253", "DF": "#dadada",
    "tDCommentF": "71", "DCommentF": "#5faf5f",
    "tDStringF": "174", "DStringF": "#d78787",
    "tDKeywordF": "183", "DKeywordF": "#d7afff",
    "tDSelectionB": "24", "DSelectionB": "#005f87",
    # "tDSelectionF": "15", "DSelectionF": "#000000",
    "tDSearchB": "241", "DSearchB": "#626262",
    "tDMatchBracketB": "25", "DMatchBracketB": "#005faf",
    "tDCurrentLineB": "238", "DCurrentLineB": "#444444",
    "tDMaxColumnB": "238", "DMaxColumnB": "#444444",
    "tDCompletePopupB": "238", "DCompletePopupB": "#444444",
    "tDCompletePopupF": "253", "DCompletePopupF": "#dadada",

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
