# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Urls(models.Model):
    url = models.URLField()
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.url
