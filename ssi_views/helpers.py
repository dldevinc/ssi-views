from django.urls import reverse

from .logging import logger
from .registry import registry


def ssi_url(name: str):
    if name not in registry:
        logger.warning("view `%s` is not registered" % name)
    return reverse("ssi_views:router", kwargs={"name": name})
