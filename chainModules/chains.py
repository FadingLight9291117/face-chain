from abc import ABC, abstractmethod


class BaseNode(ABC):
    def __init__(self, name, model=None):
        self.model = model
        self.name = name
        self.next = None

    def setNext(self, next):
        self.next = next
        return self

    def forward(self, image):
        if self.resolve(image):
            return True
        elif self.next is not None:
            return self.next(image)
        else:
            print('problem cannot be solved.')
            return False

    @abstractmethod
    def resolve(self, image):
        ...

    def __call__(self, image):
        self.forward(image)


class DemoNode(BaseNode):
    def resolve(self, image):
        if image < self.size:
            print(f'{self.name} solve the problem.')
            return True
        else:
            return False


class RetinaFaceNode(BaseNode):
    def __init__(self, name, model, *args, **kargs):
        assert model is not None
        super().__init__(name, model)
        self.model = model

    def resolve(self, image):
        model = self.model
        preds = model(image)
        ...
        return True


class LeafNode(BaseNode):
    def __init__(self, name, model, *args, **kwargs):
        assert model is not None
        super().__init__(name, model)

    def resolve(self, image):
        model = self.model
        preds = model(image)
        ...
        return True


class CabNode(BaseNode):
    def __init__(self, name, model, *args, **kwargs):
        assert model is not None
        super().__init__(name, model)

    def resolve(self, image):
        model = self.model
        preds = model(image)
        ...
        return True


class HatNode(BaseNode):
    def __init__(self, name, model, *args, **kwargs):
        assert model is not None
        super().__init__(name, model)

    def resolve(self, image):
        model = self.model
        preds = model(image)
        return True


class GlassNode(BaseNode):
    def __init__(self, name, model, *args, **kwargs):
        assert model is not None
        super().__init__(name, model)

    def resolve(self, image):
        model = self.model
        preds = model(image)
        ...
        return True


class FaceMaskNode(BaseNode):
    def __init__(self, name, model, *args, **kwargs):
        assert model is not None
        super().__init__(name, model)

    def resolve(self, image):
        model = self.model
        preds = model(image)
        ...
        return True


class HeadNode(BaseNode):
    """
     头结点负责接受参数，比如device
    """

    def resolve(self, image):
        return True


if __name__ == '__main__':
    model1 = None
    model2 = None
    model3 = None
    model4 = None
    model5 = None
    model6 = None
    retinaFaceNode = RetinaFaceNode('RetinaFace 模型', model1)
    leafNode = LeafNode('检测叶子的模型', model2)
    hatNode = HatNode('检测帽子的模型', model3)
    cabNode = CabNode('检测驾驶室的模型', model4)
    glassNode = GlassNode('检测模型的模型', model5)
    faceMaskNode = FaceMaskNode('检测口罩的模型', model6)
    headNode = HeadNode('开始')

    (
        headNode.setNext(cabNode)
            .setNext(leafNode)
            .setNext(hatNode)
            .setNext(glassNode)
            .setNext(faceMaskNode)
            .setNext(retinaFaceNode)
    )
    image = ''
    headNode(image)
