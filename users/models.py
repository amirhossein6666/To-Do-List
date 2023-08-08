from django.contrib.auth.models import AbstractUser
from django.db import models

# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)

#     # Add custom fields here, if needed
#     groups = models.ManyToManyField(
#         'auth.Group',  # Use a string to avoid circular import
#         related_name="custom_users"
#     )
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',  # Use a string to avoid circular import
#         related_name="custom_users"
#     )
#     def __str__(self):
#         return self.username