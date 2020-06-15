class Train:
    def __init__(self, uid, length, front):
        self.uid = uid
        self.train_length = length
        self.front = front


class Intersection:
    def __init__(self, uid, mutex, locked_by):
        self.uid = uid
        self.mutex = mutex
        self.locked_by = locked_by


class Crossing:
    def __init__(self, position, intersection):
        self.position = position
        self.intersection = intersection
