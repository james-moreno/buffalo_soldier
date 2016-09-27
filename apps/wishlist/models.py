from django.db import models
from ..landr.models import User
# Create your models here.


class ItemManager(models.Manager):
    def new_item(self, data, creator):
        errors = []

        if not data['product']:
            errors.append("No product given.")
        if len(data['product']) < 3:
            errors.append("Must be more than 3 characters.")

        response = {}
        if errors:
            response['errors'] = errors
            response['created'] = False
        else:
            self.create(name=data['product'], created_by=creator)
            response['created'] = True
        return response


class Item(models.Model):
    name = models.CharField(max_length=45)
    created_by = models.CharField(max_length=45)
    users = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ItemManager()
