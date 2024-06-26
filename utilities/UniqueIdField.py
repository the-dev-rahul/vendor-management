from django.db import models
import uuid

def unique_id_model():
    return models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)