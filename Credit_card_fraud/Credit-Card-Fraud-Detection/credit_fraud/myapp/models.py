from django.db import models


class TemporaryFiles(models.Model):
    file=models.FileField(upload_to="files/")

    class Meta:
        verbose_name="Temporary File"
    
    def __str__(self) -> str:
        return str(self.pk)
