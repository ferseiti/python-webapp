from django.db import models

class UserPort(models.Model):
    username = models.CharField(max_length=200)
    container_name = models.CharField(max_length=100)
    container_ip_address = models.CharField(max_length=15)
    container_port = models.IntegerField(default=0)

    def __str__(self):
        return self.username + " " + str(self.container_port)
# Create your models here.
