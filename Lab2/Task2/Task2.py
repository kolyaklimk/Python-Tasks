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

    def find(self, *keys):
        found = False
        for key in keys:
            if key in self.container:
                found = True
                print('Found', key, 'in container.')
        if not found:
            print('No such elements in container!')
    