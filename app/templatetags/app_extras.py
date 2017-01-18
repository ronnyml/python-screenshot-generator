from django import template
import base64

register = template.Library()

@register.filter()
def decode_image(encoded_image):
    return "data:image/png;base64,%s" % encoded_image.decode("utf8")
