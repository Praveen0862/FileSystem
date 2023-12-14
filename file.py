class File:
    def __init__(self, name) -> None:
        self.name = name
        self.data = None
    
    def read(self):
        return self.data
    
    def write(self, data):
        self.data = data