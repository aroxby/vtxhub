import json


def load_config(path: str = 'secrets.json') -> dict:
    """
    Example format:
        {
            "username": "aroxby@users.noreply.github.com",
            "password": "secret",
            "webapp": "example.app.vtxhub.com",
        }
    """
    with open(path, encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data
