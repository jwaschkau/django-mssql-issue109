from django.db import transaction
from django.test import TestCase

# Create your tests here.
from issue109 import models


class MyTest(TestCase):
    def test_issue_109(self):
        with transaction.atomic():
            mymodel1 = models.MyModel1.objects.create(
                field1='a',
                field2='a'
            )
            models.MyModel2.objects.create(
                field1='a',
                mymodel1=mymodel1
            )
            models.MyModel2.objects.create(
                field1='b',
                mymodel1=mymodel1
            )

            model1_result = models.MyModel1.objects.select_for_update().all()
            model2_result = models.MyModel2.objects.filter(mymodel1__in=model1_result, field1='a')
            for result in model2_result:
                print(result)
