class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        try:
            values = self.hashmap[key]
            values[timestamp] = value
            self.hashmap[key] = values
        except KeyError:
            self.hashmap[key] = {timestamp: value}

    def get(self, key: str, timestamp: int) -> str:
        try:
            values = self.hashmap[key]
        except KeyError:
            return ""
        #finding latest timestamp
        latest_timestamp = 0
        for i in values.keys():
            if timestamp >= i:
                latest_timestamp = i
        try:
            return values[latest_timestamp]
        except KeyError:
            return ""