from django.db import models

from news_app.models import News

class PublishMeneger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.status.Published)