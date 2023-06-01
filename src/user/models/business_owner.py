from django.db import models

from core.utils.base_model import BaseModel

from .base import BaseUser


class BusinessOwner(BaseModel):
    user_profile = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
