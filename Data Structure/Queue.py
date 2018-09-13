class Queue:
    def __init__(self):
        self._item = []

    def add(self, data):
        if data not in self._item:
            self._item.append(data)

    def peek(self):
        return self._item[len(self._item) - 1]

    def remove(self):
        first = self._item[0]
        del self._item[0]
        return first

    def isEmpty(self):
        return True if len(self._item) == 0 else False



q = Queue()

