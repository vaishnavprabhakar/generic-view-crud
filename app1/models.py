from django.db import models

# Create your models here.


class User(models.Model):

    username = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return self.username
    


class Poll(models.Model):

    name = models.CharField(unique=True, max_length=50)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_created=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.user