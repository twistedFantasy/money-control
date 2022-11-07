from django.db import models

from leprechaun.core.models import BaseModel


class Category(BaseModel):
    title = models.CharField("Title", max_length=32, null=False, blank=False)
