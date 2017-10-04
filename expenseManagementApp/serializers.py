from rest_framework import serializers
from expenseManagementApp.models import Expense
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    expenses = serializers.HyperlinkedRelatedField(queryset=Expense.objects.all(), view_name='expense-detail', many=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'expenses')

class ExpenseSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Expense
		fields =  ('expenseTitle', 'date', 'amount', 'currency', 'paymentType', 'creditCardOrBankAccountNo', 'expenseType', 'currency', 'vendorName', 'invoiceId')

