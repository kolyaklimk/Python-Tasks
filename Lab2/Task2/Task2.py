class MyContainer:
    def __init__(self):
        self.container = set()

    def add(self, *keys):
        for key in keys:
            if key not in self.container:
                self.container.add(key)

    def remove(self, key):
        if key in self.container:
            self.container.remove(key)
   