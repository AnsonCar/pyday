class Test01:
    def __init__(self):
        self.path = "./test"

class Test02(Test01):
    def __init__(self):
        super().__init__()
        # self.path = "./test"