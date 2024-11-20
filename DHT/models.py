from django.db import models

class Dht11(models.Model):
    temp = models.FloatField(null=True, blank=True)  # Permettre des valeurs nulles et des champs vides
    hum = models.FloatField(null=True, blank=True)
    dt = models.DateTimeField(auto_now_add=True)  # Enregistre automatiquement la date et l'heure lors de la création

    def __str__(self):
        return f"Température: {self.temp}°C, Humidité: {self.hum}%, Date: {self.dt}"
