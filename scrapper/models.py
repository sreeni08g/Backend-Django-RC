from django.contrib.postgres.fields import ArrayField
from django.db import models
# Create your models here.


class QueryHistory(models.Model):
    id = models.AutoField(primary_key=True)
    query = models.CharField(max_length=100)
    date_create = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    #exams_applicable = ArrayField(models.CharField(max_length=100),  default=list)

    # def __str__(self):
    #     """Return a human readable representation of the model instance."""
    #     return "{}".format(self.id)