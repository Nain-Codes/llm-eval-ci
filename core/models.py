from django.db import models

# class BizNeed(models.Model):
#     id = models.ObjectIdField(primary_key=True)
#     description = models.CharField(max_length=255)
#     deliveryProduct = models.CharField(max_length=255)
#     userId = models.ForeignKey(User, on_delete=models.CASCADE)
#     customFields = django_models.JSONField()
#     businessObjectiveId = models.ForeignKey(BusinessObjective, on_delete=models.CASCADE)
    
#     class Meta:
#         db_table = 'bizneeds'