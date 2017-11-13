from django.db import models
from django.utils import timezone


class Magazine(models.Model):
    title = models.CharField('OFF Magazine', max_length=100)
    pub_date = models.DateTimeField('Publish Date', default=timezone.now)

    # Magazine PDF FILE #
    file = models.FileField(
        upload_to='magazines/'
    )

    def __str__(self):
        return self.title
