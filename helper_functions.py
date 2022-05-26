import yaml


def read_yaml(file):
    with open(file) as file:
        config = yaml.safe_load(file)

    return config
