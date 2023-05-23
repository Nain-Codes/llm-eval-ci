from django.db import models
from djongo import models
from django.contrib.auth.models import User


class ProfitCenter(models.Model):
    profitCenterName = models.CharField(max_length=255)
    description = models.TextField()
    userId = models.ForeignKey(User, on_delete=models.CASCADE)

class Meta:
    db_table = 'profit_centers'


class BusinessObjective(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    metric = models.CharField(max_length=255)
    businessMeasurement = models.CharField(max_length=255)
    changeStatus = models.CharField(max_length=255)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    profitCenterId = models.ForeignKey(ProfitCenter, on_delete=models.CASCADE)
class Meta:
    db_table = 'business_objectives'


class BizNeed(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    description = models.CharField(max_length=255)
    deliveryProduct = models.CharField(max_length=255)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    Jsonfield = models.JSONField()
    businessObjectiveId = models.ForeignKey(BusinessObjective, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'bizneeds'





