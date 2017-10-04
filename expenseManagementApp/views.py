# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from expenseManagementApp.models import Expense
# from expenseManagementApp.serializers import ExpenseSerializer
# from django.contrib.auth.models import User
# from rest_framework.decorators import api_view
# from rest_framework.response import Response


# class ExpenseList(APIView):
#     """
#     List all code expense, or create a new expense.
#     """
#     def get(self, request, format=None):
#         expenses = Expense.objects.all()
#         serializer = ExpenseSerializer(expenses, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = ExpenseSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ExpenseDetail(APIView):
#     """
#     Retrieve, update or delete a expense instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Expense.objects.get(pk=pk)
#         except Expense.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         expense = self.get_object(pk)
#         serializer = ExpenseSerializer(expense)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         expense = self.get_object(pk)
#         serializer = ExpenseSerializer(expense, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         expense = self.get_object(pk)
#         expense.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




# from expenseManagementApp.models import Expense
# from expenseManagementApp.serializers import ExpenseSerializer, UserSerializer
# from rest_framework import generics
# from django.contrib.auth.models import User

# class ExpenseList(generics.ListCreateAPIView):
#     queryset = Expense.objects.all()
#     serializer_class = ExpenseSerializer
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


# class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Expense.objects.all()
#     serializer_class = ExpenseSerializer

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from expenseManagementApp.models import Expense
from expenseManagementApp.permissions import IsOwnerOrReadOnly
from expenseManagementApp.serializers import ExpenseSerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from rest_framework import filters, viewsets, generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
import datetime

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'expenses': reverse('expense-list', request=request, format=format)
    })


class ExpenseViewSet(viewsets.ModelViewSet):
    
    serializer_class = ExpenseSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def get_queryset(self) :
        myUser = self.request.user
        querydata = Expense.objects.all().filter(owner = myUser)
        month = self.request.query_params.get('month', None)
        date = self.request.query_params.get('date', None)
        finalData = []
        if date is not None:
            querydata = querydata.filter(date=date)
        if month is not None:
            for data in querydata:
                datee = str(data.date)
                day = datee.split('-')
                if len(day) > 1:
                    print(day[1])
                    if month == day[1]:
                        finalData.append(data)
            querydata = finalData
        return querydata

    

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        expense = self.get_object()
        return Response(expense.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
class UserViewSet(viewsets.ReadOnlyModelViewSet ):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
def user_expense(request):
    return None
