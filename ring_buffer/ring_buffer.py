class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.index = 0

    def append(self, item):
        if len(self.data) == self.capacity:
            self.data[self.index] = item
            if self.index + 1 == self.capacity:
                self.index = 0
            else:
                self.index += 1
        else:
            self.data.append(item)

    def get(self):
        return self.data
