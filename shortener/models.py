# Django packages
from django.db import models
# Third party apps
import re
import random


class LinkShortener(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, null=True, blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        url = re.search('\w+.com', self.long_url)
        return self.long_url

    @staticmethod
    def random_char():
        chars = 'ABCDEFGHJKLMNOPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
        length = 6
        link = "".join(random.sample(chars, length))
        return link

    @classmethod
    def create_short_url(cls, long_url):
        rand_text = cls.random_char()
        if not cls.objects.filter(short_url=rand_text).exists():
            return cls.objects.create(
                long_url=long_url,
                short_url=cls.random_char()
            )

    def create_auto_short_url(self):
        if not self.short_url:
            rand_text = self.random_char()
            if not LinkShortener.objects.filter(short_url=rand_text).exists():
                self.short_url = rand_text
                self.save()
