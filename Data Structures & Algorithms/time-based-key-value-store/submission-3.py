class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = {timestamp: value}
        else:
            self.store[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        latesttime = 0
        for time in self.store[key]:
            if time <= timestamp:
                latesttime = time

        if latesttime != 0:
            return self.store[key][latesttime]
        else:
            return ""

