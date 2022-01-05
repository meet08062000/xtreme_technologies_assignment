from django.db import models
from django.core.mail import send_mail
from mail_weather.views import get_weather_data
from django.conf import settings


class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    city = models.CharField(max_length=20, choices=[(
        'Mumbai', 'Mum'), ('Delhi', 'Del'), ('Chennai', 'Che'), ('Bangalore', 'Ban'), ('Kolkata', 'Kol')])
    time = models.TimeField(editable=False, auto_now_add=True)

    def save(self, *args, **kwargs):
        temp = get_weather_data(self.city)
        temp = round(temp - 273.15)
        if temp <= 15:
            emoji = u"\U0001F976"
        elif temp > 15 and temp <= 30:
            emoji = u"\U0001F642"
        else:
            emoji = u"\U0001F975"
        send_mail(
            'Hi ' + self.username + ', interested in our services',
            str(temp) + '°C' + emoji,
            settings.EMAIL_HOST_USER,
            [self.email],
            fail_silently=False,
        )
        super(User, self).save(*args, **kwargs)
