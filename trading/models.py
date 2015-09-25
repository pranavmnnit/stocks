from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

# Create your models here.

class Trader(models.Model):
    # ...
	def __str__(self):
	    return self.name
	
	name = models.CharField(max_length=200)
	org_name = models.CharField(max_length=100)
	mobile = models.IntegerField(default=0)
	e_mail = models.EmailField(max_length=100)
	points = models.IntegerField(default=0)

class Stock(models.Model):
    # ...
    def __str__(self):
	    return self.stock_name
    trader = models.ForeignKey(Trader)
    stock_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    cur_price = models.FloatField(default=0)
    predict_price = models.FloatField(default=0)
    Rating = models.IntegerField(
	    validators = [MinValueValidator(0), MaxValueValidator(10)])

class Viewer(models.Model):
    # ...
    def __str__(self):
	    return self.name
    name = models.CharField(max_length=200)
    mobile = models.IntegerField(default=0)
    e_mail = models.CharField(max_length=100)
    credits = models.IntegerField(default=0)
