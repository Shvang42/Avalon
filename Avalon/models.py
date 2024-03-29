from django.db import models



class User(models.Model):
    user_id = models.CharField(max_length=30, primary_key=True, unique=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now=True)
    lobby_id = models.CharField(max_length=50, null=True)
    card_id = models.IntegerField(max_length=2, null=True)

class Lobby(models.Model):
    lobby_name = models.CharField(max_length=30)
    lobby_code = models.CharField(max_length=30, primary_key=True, unique=True)
    lobby_users = models.JSONField(default=list)
    lobby_host = models.JSONField(max_length=50)
    lobby_host_id = models.JSONField(max_length=50)
    lobby_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.lobby_name} {self.lobby_code} {self.lobby_users} {self.lobby_host} {self.lobby_date}"
    
class Card(models.Model):
    card_name = models.CharField(max_length=30, primary_key=True, unique=True)
    card_num = models.IntegerField(max_length=2)
    card_description = models.CharField(max_length=100)
    card_color = models.BooleanField()
