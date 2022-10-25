from django.db import models
# Third party apps
import re


class LinkShortener(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, null=True, blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        url = re.search('\w+.com', self.long_url)
        return self.long_url
