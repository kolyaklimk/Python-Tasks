from django.db import models


# https://django.fun/ru/docs/django/4.1/topics/db/models/
# https://django.fun/ru/docs/django/4.1/ref/models/fields/#model-field-types
class TypeRoom(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Room(models.Model):
    type = models.ForeignKey(TypeRoom, on_delete=models.CASCADE)
    capacity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return f"Room {self.id}"


class Payment(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class Client(models.Model):
    last_name = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, blank=True)
    patronymic = models.CharField(max_length=100, blank=True)
    commentary = models.TextField()
    has_child = models.BooleanField(blank=True)
    payment_type = models.ManyToManyField(Payment, blank=True)

    def __str__(self):
        return f"{self.last_name} {self.name}"


class Period(models.Model):
    check_in_date = models.DateField(blank=True)
    eviction_date = models.DateField(blank=True)

    def __str__(self):
        return f"Check-in: {self.check_in_date}; Eviction: {self.eviction_date}"


class Reservation(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    residence_period = models.OneToOneField(Period, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reservation {self.id}"
