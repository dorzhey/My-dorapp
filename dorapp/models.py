from django.db import models
from django.utils import timezone

# Create your models here.
class tool(models.Model):
    tool_name = models.CharField(max_length = 20)
    description = models.CharField(max_length = 30)
    stock_date = models.DateTimeField(default = timezone.now)
    
    def stock(self):
        self.save()
    def __str__(self):
        return self.tool_name