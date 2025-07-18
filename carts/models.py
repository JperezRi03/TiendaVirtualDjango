from django.db import models
from orden.comun import OrdenStatus
from users.models import User
from products.models import Product
from django.db.models.signals import pre_save, m2m_changed , post_save
import uuid , decimal
# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartProduct')
    subtotal = models.DecimalField(default=0.0, max_digits=8, decimal_places=2) # type: ignore
    total = models.DecimalField(default=0.0, max_digits=8, decimal_places=2) # type: ignore
    created_at = models.DateTimeField(auto_now_add=True)
    FEE = 0.01

    def __str__(self): # type: ignore
        return self.cart_id
    
    def update_totals(self):
        self.update_subtotal()
        self.update_total()
        if self.orden:
            self.update_total()

    def update_subtotal(self):
        self.subtotal = sum([
            i.quantity * i.product.price for i in self.product_related()
        ])
        self.save()

    def update_total(self):
        self.total = self.subtotal + (self.subtotal * decimal.Decimal(Cart.FEE))
        self.save()

    def product_related(self):
        return self.cartproduct_set.select_related('product') # type: ignore
    
    @property
    def orden(self):
        return self.orden_set.filter(status= OrdenStatus.CREATED).first # type: ignore

class CartProductManager(models.Manager):
    def crearActualizar(self,cart,product,quantity=1):
        object,created = self.get_or_create(cart=cart, product=product)
        if not created:
            quantity = object.quantity + quantity
        object.update_quantity(quantity)
        return object

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 1)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = CartProductManager()
    def update_quantity(self, quantity=1):
        self.quantity = quantity
        self.save()


def set_cart_id(sender,instance, *args,**kwargs):
    if not instance.cart_id:
        instance.cart_id = str(uuid.uuid4())

def update_totals(sender, instance, action , *args, **kwargs ):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        instance.update_totals()

def postActualizar(sender, instance, *args , **kwargs):
    instance.cart.update_totals()


post_save.connect(postActualizar, sender = CartProduct)
pre_save.connect(set_cart_id, sender=Cart)
m2m_changed.connect(update_totals, sender=Cart.products.through)