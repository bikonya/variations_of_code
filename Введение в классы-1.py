class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.now = 0

    def can_add(self, v):
        if self.now + v <= self.capacity:
            return True
        else:
            return False

    def add(self, v):
        if self.can_add(v) is True:
            self.now += v
            return True
        else:
            return False