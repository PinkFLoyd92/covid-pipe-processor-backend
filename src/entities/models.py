from django.db import models
from datetime import datetime


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Location(TimeStampedModel):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name_plural = "Locations"

    def __str__(self):
        return self.name


class Movement(TimeStampedModel):
    CREATED = 1
    SENT = 2
    STATES = (
        (CREATED, 'A ENVIAR'),
        (SENT, 'ENVIADO'),
    )
    date_sent = models.DateField(null=True, blank=True)
    date_created = models.DateField(null=True, blank=True)
    state = models.PositiveSmallIntegerField(
        choices=STATES, default=CREATED)
    description = models.CharField(
        max_length=200, default='',
        blank=True,)
    origin = models.ForeignKey(
        Location, on_delete=models.PROTECT, related_name="movement_origin",
        null=True, default=None)
    destination = models.ForeignKey(
        Location, on_delete=models.PROTECT, related_name="movement_destination",
        null=True, default=None)
    pipe = models.ForeignKey(
        'CovidPipe', on_delete=models.CASCADE,
        null=True, blank=True,
        related_name="movement")
    date = models.DateTimeField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        super(Movement, self).save(*args, **kwargs)
        self.pipe.last_movement = self
        self.pipe.save()

    def __str__(self):
        return "Origen: {}, Destino: {} CovidPipe: {}, fecha: {}".format(self.origin, self.destination, self.pipe, self.date)


class CovidPipe(TimeStampedModel):
    con_muestra = models.BooleanField(default=False)
    name = models.CharField(
        max_length=50, default='',
        blank=True, unique=True)

    alias = models.ForeignKey(
        'CovidPipe', on_delete=models.PROTECT,
        related_name="last_pipe", blank=True, null=True)

    last_movement = models.ForeignKey(
        'Movement', on_delete=models.SET_NULL,
        related_name="last_movement", blank=True, null=True)

    class Meta:
        verbose_name_plural = 'pipes'
        ordering = ['-name']

    def __str__(self):
        return self.name
