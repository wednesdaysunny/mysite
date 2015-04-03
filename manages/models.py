from django.db import models

# Create your models here.
class Good(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    created_at = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.name