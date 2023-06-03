from django.db import models


# https://django.fun/ru/docs/django/4.1/topics/db/models/
# https://django.fun/ru/docs/django/4.1/ref/models/fields/#model-field-types
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Room(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)

    def __str__(self):
        return f"Room {self.id} ({self.category})"


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    has_child = models.BooleanField(blank=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    def __str__(self):
        return f"Booking {self.id} - {self.client} ({self.room})"
