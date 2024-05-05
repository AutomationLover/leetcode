# https://leetcode.cn/problems/design-circular-queue/description/
# 如何判断队列空和队列满，常见的方法有两种：

# 留一个空位，队头队尾指针重合为空，队头指针在队尾指针前面一个位置为满
# 用一个变量记录队列中元素数量
class MyCircularQueue:

    def __init__(self, k: int):
        self.front = self.rear = 0
        self.data = [-1] * (k + 1)

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.data[self.rear] = value
        self.rear = (self.rear + 1) % len(self.data)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        val = self.data[self.front]
        self.front = (self.front + 1) % len(self.data)
        return True

    def Front(self) -> int:
        return self.data[self.front] if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.data[(self.rear - 1) % len(self.data)] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.rear == self.front

    def isFull(self) -> bool:
        return (self.rear + 1) % len(self.data) == self.front


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()


class MyCircularQueue2:

    def __init__(self, k: int):
        self.st = [0] * k
        self.top, self.tail, self.size, self.length = -1, 0, 0, k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.top = (self.top + 1) % self.length
        self.st[self.top] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.tail = (self.tail + 1) % self.length
        self.size -= 1
        return True

    def Front(self) -> int:
        return self.st[self.tail] if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.st[self.top] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size >= self.length

