from importlib import resources
import yaml


def read_yaml(folder_path, file_name):
    try:
        with resources.open_text(folder_path, file_name) as file:
            yaml_file = dict(yaml.safe_load(file.read()))
        return yaml_file
    except FileNotFoundError as e:
        print(f"file not found: {file_name}: {e}")
