from django.db import models


class Driver(models.Model):
    driver_id = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=100)
    number = models.IntegerField(null=True, blank=True)
    nationality = models.CharField(max_length=50)
    headshot_url = models.URLField(blank=True)

class Constructor(models.Model):
    constructor_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)
    logo_url = models.URLField(blank=True)

class Season(models.Model):
    year = models.IntegerField(unique=True)

class Race(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    circuit = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    date = models.DateField()

class Result(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    constructor = models.ForeignKey(Constructor, on_delete=models.CASCADE)

    position = models.IntegerField(null=True, blank=True)
    grid = models.IntegerField(null=True, blank=True)
    points = models.FloatField(default=0)

    laps = models.IntegerField(null=True, blank=True)
    fastest_lap = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=100, blank=True)

class LapData(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

    lap_number = models.IntegerField()
    lap_time = models.FloatField(null=True, blank=True)

    sector1_time = models.FloatField(null=True, blank=True)
    sector2_time = models.FloatField(null=True, blank=True)
    sector3_time = models.FloatField(null=True, blank=True)

    compound = models.CharField(max_length=30, blank=True)
    tyre_life = models.IntegerField(null=True, blank=True)

class PitStop(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

    lap = models.IntegerField()
    duration = models.FloatField()

class Prediction(models.Model):
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="predictions"
    )

    driver = models.ForeignKey(
        Driver,
        on_delete=models.CASCADE,
        related_name="predictions"
    )

    predicted_position = models.IntegerField()

    win_probability = models.FloatField(
        null=True,
        blank=True
    )

    podium_probability = models.FloatField(
        null=True,
        blank=True
    )

    predicted_points = models.FloatField(
        null=True,
        blank=True
    )

    actual_position = models.IntegerField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )