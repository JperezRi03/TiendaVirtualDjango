from django.db import models
from users.models import User

class DireccionEnvio(models.Model):
    user = models.ForeignKey(User , null=False , blank=False, on_delete=models.CASCADE)
    line1 = models.CharField(max_length= 300)
    line2 = models.CharField(max_length= 300, blank=True)
    city = models.CharField(max_length= 100)
    state = models.CharField(max_length= 100)
    coutry= models.CharField(max_length= 50)
    reference = models.CharField(max_length= 300)
    postal_code = models.CharField(max_length= 10, null=False , blank=False)
    default = models.BooleanField(default=False)
    created_ad = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.postal_code
    
    def update_default(self, default=False):
        self.default = default
        self.save()

    def has_orden(self):
        return self.orden_set.count() >= 1 # type: ignore

    @property
    def direccion(self):
        return '{}-{}-{}'.format(self.city , self.state, self.coutry)