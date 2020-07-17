class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.old = 0

    def append(self, item):
        if len(self.data) == self.capacity:
            self.data[self.old] = item
            if self.old + 1 == self.capacity:
                self.old = 0
            else:
                self.old += 1
        else:
            self.data.append(item)

    def get(self):
        return self.data
