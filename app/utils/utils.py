import yaml

__all__ = ("load_config",)


def load_config(path: str) -> dict:
    with open(path, "r") as file:
        return yaml.safe_load(file)
