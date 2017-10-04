from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Expense(models.Model):
	PAYMENT_CHOICES = (
		('CREDITCARD' , 'creditCard'),
		('DEBITCARD' , 'debitCard'),
		('NETBANKING' , 'netBanking'),
		('CASH' , 'cash'),
		('OTHERS' , 'others')
		)

	EXPENSE_CHOICES = (
		( 'FAMILY', 'family' ),
		( 'PERSONAL', 'personal' ),
		( 'BUSINESS', 'business' ),
		( 'OTHERS', 'others' )
		)

	owner = models.ForeignKey('auth.User', related_name = 'expenses', on_delete=models.CASCADE)
	expenseTitle = models.CharField(max_length=200)
	date = models.DateField(null=True)
	amount = models.IntegerField(max_length=200)
	currency = models.CharField(max_length=200)
	paymentType = models.CharField(max_length=10, choices=PAYMENT_CHOICES, default='CREDITCARD')
	creditCardOrBankAccountNo = models.CharField(max_length=200)
	expenseType = models.CharField(max_length=200, choices=EXPENSE_CHOICES, default='FAMILY')
	currency = models.CharField(max_length=200)
	vendorName = models.CharField(max_length=200)
	invoiceId = models.IntegerField(max_length=200)

			
