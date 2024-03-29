import json
import os
import re


class MyContainer:
    def __init__(self, username):
        self.container = set()
        self.username = username

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

    def list(self):
        for key in self.container:
            print(key)

    def grep(self, regex):
        found = False
        re_pattern = re.compile(regex)
        for key in self.container:
            if re_pattern.search(key):
                print(key)
                found = True
        if not found:
            print('No such elements in container!')

    def save(self, files):
        os.makedirs(os.path.dirname(f'./users/{files}.json'), exist_ok=True)
        with open(f'./users/{files}.json', 'w') as file:
            json.dump(list(self.container), file)

    def load(self, files):
        if os.path.exists(f'./users/{files}.json'):
            with open(f'./users/{files}.json', 'r') as file:
                self.container.update(set(json.load(file)))
        else:
            print('No save with', files)

    def switch(self, username):
        if input(f'Save {self.username} container?(y/n)') == 'y':
            self.save(self.username)
        self.username = username
        self.container.clear()
        if input(f'Load {self.username} container?(y/n)') == 'y':
            self.load(self.username)
