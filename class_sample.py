class Sample2():

    def __init__(self,value_A: int, value_b: int) :
        self.value_a = value_A
        self.__value_b = value_b

    @property
    def valuetype(self):
        return type(self.value_a)

    @property
    def value_b(self):
        return self._x      # getter

    @value_b.setter
    def value_b(self, value):
        self._x = value     # setter

if __name__ == '__main__':
    sample = ()

