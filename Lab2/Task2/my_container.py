import json
import os
import re


class MyContainer:
    def __init__(self, username):
        self.container = set()
        self.username = username

    def add(self, *keys):
        for key in keys:
            if str(key) not in self.container:
                self.container.add(str(key))

    def remove(self, key: str):
        if key in self.container:
            self.container.remove(key)

    def find(self, *keys):
        found = False
        for key in keys:
            if str(key) in self.container:
                found = True
                print('Found', str(key), 'in container.')
        if not found:
            print('No such elements in container!')

    def list(self):
        for key in self.container:
            print(key)

    def grep(self, regex: str):
        found = False
        re_pattern = re.compile(regex)
        for key in self.container:
            if re_pattern.search(key):
                print(key)
                found = True
        if not found:
            print('No such elements in container!')

    def save(self):
        os.makedirs(os.path.dirname(f'./users/{self.username}.json'), exist_ok=True)
        with open(os.path.dirname(f'./users/{self.username}.json'), 'r') as file:
            json.dump(list(self.username), file)

    def load(self):
        if os.path.exists(f'./users/{self.username}.json'):
            with open(os.path.dirname(f'./users/{self.username}.json'), 'r') as file:
                self.container.update(set(json.load(file)))
        else:
            print('No save with', self.username)

    def switch(self, username: str):
        if input(('Save', self.container, 'container?(y/n)')) == 'y':
            self.save()
        self.username = username
        self.container.clear()
        if input(('Load', self.container, 'container?(y/n)')) == 'y':
            self.load()
