class Directory:
    def __init__(self, name, path, parent=None) -> None:
        self.name = name
        self.parent = parent
        self.dirpath = path
        self.contents = {}
        if parent:
            self.contents = {
                '.' : self,
                '..' : parent
            }