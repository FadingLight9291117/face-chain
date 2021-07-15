from abc import ABC, abstractmethod


class BaseNode(ABC):
    def __init__(self, name, pixels):
        self.size = pixels
        self.name = name
        self.next = None

    def setNext(self, next):
        self.next = next
        return self

    def support(self, image):
        if self.resovle(image):
            return True
        elif self.next is not None:
            return self.next(image)
        else:
            print('problem cannot be solved.')
            return False

    @abstractmethod
    def resovle(self, image):
        ...

    def __call__(self, image):
        self.support(image)


class DemoNode(BaseNode):
    def resovle(self, image):
        if image < self.size:
            print(f'{self.name} solve the problem.')
            return True
        else:
            return False


if __name__ == '__main__':
    node1 = DemoNode('1', 10)
    node2 = DemoNode('2', 50)
    node3 = DemoNode('3', 100)
    node4 = DemoNode('4', 500)

    (node1.setNext(node2)
     .setNext(node3)
     .setNext(node4))

    node1(300)
