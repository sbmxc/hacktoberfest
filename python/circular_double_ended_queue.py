class CircularDeque:
    """
    A circular double ended queue.
    """
    def __init__(self, k: int):
        self.k = k
        self.counter = 0
        self._queue = []
    def insert_front(self, value: int) -> bool:
        """
        Inserts a given value to the front of the circular double ended queue.
        """
        if not self.is_full():
            self._queue.insert(0, value)
            self.counter += 1
            return True
        else:
            return False
    def insert_last(self, value: int) -> bool:
        """
        Inserts a given value at the end of the circular double ended queue.
        """
        if not self.is_full():
            self._queue.append(value)
            self.counter += 1
            return True
        else:
            return False
    def delete_front(self) -> bool:
        """
        Deletes the value at the front of the circular double ended queue.
        """
        try:
            self._queue.pop(0)
            self.counter -= 1
            return True
        except IndexError:
            return False
    def delete_last(self) -> bool:
        """
        Deletes the value at the end of the circular double ended queue.
        """
        try:
            self._queue.pop()
            self.counter -= 1
            return True
        except IndexError:
            return False
    def get_front(self) -> int:
        """
        Returns the value at the front of the circular double ended queue.
        """
        try:
            return self._queue[0]
        except IndexError:
            return None
    def get_rear(self) -> int:
        """
        Returns the value at the rear of the circular double ended queue.
        """
        try:
            return self._queue[-1]
        except IndexError:
            return None
    def is_empty(self) -> bool:
        """
        Returns a boolean that determines whether the queue is empty.
        """
        return self.counter == 0
    def is_full(self) -> bool:
        """
        Returns a boolean that determines whether the queue is full.
        """
        return self.counter == self.k
    def __len__(self):
        return self.counter

if __name__ == "__main__":
    cdq  = CircularDeque(5)
    cdq.insert_front(4)
    cdq.insert_last(7)
    print(cdq.get_front())
    print(cdq.get_rear())
    print(len(cdq))
    print(cdq.is_full())
    cdq.delete_front()
    cdq.delete_last()
    print(cdq.is_empty())
