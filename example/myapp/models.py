from __future__ import unicode_literals

from django.db import models


def file_using_key_path(instance, filename):
    return '{0}/{1}'.format(instance.key, filename)


class FineFile(models.Model):
    key = models.CharField(max_length=20)
    fine_file = models.FileField(upload_to=file_using_key_path)

    def __str__(self):
        return self.fine_file.name
