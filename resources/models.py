from django.db import models
from accounts.models import User
# Create your models here.

class Resource(models.Model):
    resource_name= models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    qty = models.IntegerField()
    per_qty_value = models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self) -> str:
        return f"{self.resource_name, self.model, self.qty}"

class IssuedResource(models.Model):
    resource = models.ForeignKey(Resource,  on_delete=models.CASCADE,related_name='user_resource')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_resource')
    qty = models.PositiveIntegerField(default=0)
    issued_on = models.DateTimeField(auto_now_add=True)
    # returned_on = models.DateTimeField(default=None, null=True)
    def __str__(self) -> str:
        return f"{self.user.username, self.resource.resource_name}"
