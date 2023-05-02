from collections import deque
from typing import Generic, Iterator, TypeVar

T = TypeVar("T")


class CyclicBuffer(Generic[T]):
    def __init__(self, capacity: int):
        self.items = deque(maxlen=capacity)
        self.capacity = capacity

    def __len__(self):
        return len(self.items)

    def __iter__(self) -> Iterator[T]:
        return iter(self.items)

    def clear(self) -> None:
        self.items.clear()

    def push(self, item: T) -> None:
        if len(self.items) == self.capacity:
            self.items.popleft()
        self.items.append(item)
