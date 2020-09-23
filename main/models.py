from django.db import models

# Create your models here.

class todo(models.Model):
    added_date = models.DateTimeField()
    text = models.CharField(max_length=560)

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = "List"
    