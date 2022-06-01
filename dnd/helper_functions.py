from importlib import resources
import yaml


def readYaml(folder_path, file_name):
    try:
        with resources.open_text(folder_path, file_name) as file:
            yaml_file = dict(yaml.safe_load(file.read()))
        return yaml_file
    except FileNotFoundError as e:
        print(f"file not found: {file_name}: {e}")


def calculateAttributeModifier(attribute):
    attributeModifiers = {
        1: -5,
        2: -4,
        3: -4,
        4: -3,
        5: -3,
        6: -2,
        7: -2,
        8: -1,
        9: -1,
        10: 0,
        11: 0,
        12: +1,
        13: +1,
        14: +2,
        15: +2,
        16: +3,
        17: +3,
        18: +4,
        19: +4,
        20: +5
    }

    return attributeModifiers.get(attribute)


def calculateProficiencyBonus(level):
    proficiency = {
        1: +2,
        2: +2,
        3: +2,
        4: +2,
        5: +3,
        6: +3,
        7: +3,
        8: +3,
        9: +4,
        10: +4,
        11: +4,
        12: +4,
        13: +5,
        14: +5,
        16: +5,
        17: +6,
        18: +6,
        19: +6,
        20: +6,
    }

    return proficiency.get(level)
