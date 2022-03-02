from django.db import models

# Create your models here.

class MyModel1(models.Model):
    class Meta:
        ordering = (
            'field1',
        )

    field1 = models.CharField(max_length=128)
    field2 = models.CharField(max_length=128)


class MyModel2(models.Model):
    class Meta:
        ordering = (
            'field1',
        )

    field1 = models.CharField(max_length=128)
    field2 = models.CharField(max_length=128)
    mymodel1 = models.ForeignKey(MyModel1, on_delete=models.CASCADE)
