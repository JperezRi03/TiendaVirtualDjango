from django.db import models
from users.models import User

# Create your models here.
class ProfilePago(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=50, null=False, blank=False)
    card_id = models.CharField(max_length=50, blank=False, null=False)
    last4 = models.CharField(max_length=50, blank=False, null=False)
    brand = models.CharField(max_length=10, blank=False, null=False)
    default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.card_id