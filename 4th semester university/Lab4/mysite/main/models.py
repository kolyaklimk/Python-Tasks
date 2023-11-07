from django.db import models


class Milliseconds(models.Model):
    static_variable = 3000

    @classmethod
    def get_static_variable(cls):
        return cls.static_variable

    @classmethod
    def set_static_variable(cls, value):
        cls.static_variable = value
