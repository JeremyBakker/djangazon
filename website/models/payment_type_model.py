"""
djangazon model configuration for payment type
"""

from django.db import models

from website.models.profile_model import Profile


class PaymentType(models.Model):
    """
    This class models a payment type in the API's database. 

    ----Fields---- 
    account_label(character): name of payment 
    account_type(character): type of payment
    account_number(decimal): account number
    profile_id(foreign key): links to Customer(CustomerID) with a foregin key

    Author: Jeremy Bakker  
    """
    
    account_nickname = models.CharField(max_length=20)
    account_type = models.CharField(max_length=20)
    account_number = models.DecimalField(max_digits=20, decimal_places=0)
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
