import json


class JsonUtils:
    @staticmethod
    def is_json(file: str) -> bool:
        """Checking if file is json"""
        try:
            json.loads(file)
        except ValueError:
            return False
        return True
