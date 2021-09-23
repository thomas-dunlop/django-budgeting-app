from django.db import models

# Create your models here.
class Envelope(models.Model):
    env_name = models.CharField(max_length=200)
    env_budget = models.DecimalField(max_digits=1000, decimal_places=2)
    env_funds = models.DecimalField(max_digits=1000, decimal_places=2)

    def __str__(self):
        return self.env_name

class Transaction(models.Model):
    env = models.ForeignKey(Envelope, on_delete=models.CASCADE)
    t_date = models.DateTimeField('transaction date')
    amount = models.DecimalField(max_digits=1000, decimal_places=2)
    recipient = models.CharField(max_length=200)
    
    def __str__(self):
        return self.recipient