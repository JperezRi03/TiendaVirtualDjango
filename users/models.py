from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE


# Create your models here.

class User(AbstractUser):

    def get_full_name(self) -> str: # type: ignore
        def get_full_name(self):
            return '{} , {}'.format(self.firt_name , self.last_name)


    @property
    def direccion_envio(self):
        return self.direccionenvio_set.filter(default = True).first() # type: ignore
    
    def has_direccion_envio(self):
        return self.direccion_envio is not None

class Cliente(User):
    class Meta: 
        proxy = True

    
    def get_product(self):
        return [] 
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    biografia = models.TextField()
