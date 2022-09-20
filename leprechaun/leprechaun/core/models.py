from urllib.parse import urlencode

from django.db import models
from model_utils import Choices


STATUS = Choices("pending", "processing", "stopped", "failed", "completed")


class BaseModel(models.Model):
    """
    Add created and modified indexed fields
    """

    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True
