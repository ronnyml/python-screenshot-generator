from django.core.files.base import ContentFile
from django import template
from app.models import *
import base64

from django.core.files.base import ContentFile

register = template.Library()

@register.filter()
def decode_image(encoded_image):
    return "data:image/png;base64,%s" % encoded_image.decode("utf8")
