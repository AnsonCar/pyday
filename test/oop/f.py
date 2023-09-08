class Test01:
    def __init__(self):
        self.path = "./test"

    def setPath(self):
        print("this is the the super function")
class Test02(Test01):
    def __init__(self):
        super().__init__()
        # self.path = "./test"
        
test = Test02()
test1 = Test02()
test.setPath()
test1.setPath()