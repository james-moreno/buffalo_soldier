from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.

class UserManager(models.Manager):
    def new_user(self, data):
        errors = []

        if not data['name']:
            errors.append("Name can not be blank.")
        if len(data['name']) < 3:
            errors.append("Name must be longer than 3 characters")
        if not data['username']:
            errors.append("Username can not be blank.")
        if len(data['username']) < 3:
            errors.append("Username must be longer than 3 characters")
        if not data['email']:
            errors.append("Email can not be blank.")
        elif not EMAIL_REGEX.match(data['email']):
            errors.append("Invalid Email")
        if not data['password']:
            errors.append("Password can not be blank.")
        elif len(data['password']) < 8:
            errors.append("Password must be longer than 8 characters.")
        if not data['con_password']:
            errors.append("Confirm Password can not be blank.")
        if data['password'] != data['con_password']:
            errors.append("Passwords do not match.")
        if len(data['bday']) < 1:
            errors.append("Invalid Date.")

        response = {}
        if errors:
            response['errors'] = errors
            response['created'] = False
        else:
            password = data['password'].encode()
            hashed = bcrypt.hashpw(password, bcrypt.gensalt())
            new_user = self.create(name=data['name'], username=data['username'], email=data['email'], password=hashed, bday=data['bday'])
            response['created'] = True
            response['new_user'] = new_user

        return response

    def login(self, data):
        errors = []

        if not data['log_email']:
            errors.append("No email was given.")
        if not data['log_password']:
            errors.append("No password was given.")

        response = {}
        if errors:
            response['errors'] = errors
            response['log_in'] = False

        else:
            try:
                user = User.objects.get(email=data['log_email'])
                password = data['log_password'].encode()
                if bcrypt.hashpw(password, user.password.encode()) == user.password.encode():
                    response['log_in'] = True
                    response['user'] = user
            except:
                errors.append("Email does not exist.")
                response['errors'] = errors
                response['log_in'] = False

        return response


class User(models.Model):
    name = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    bday = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
