from tests.OOPClass import Calculator


class ChildClass(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 3)

    def get_data_child(self):
        return self.num2 + self.num + self.sum2numbers()


obj_child = ChildClass()
print(obj_child.get_data_child())
