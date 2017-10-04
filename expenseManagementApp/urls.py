from django.conf.urls import url, include
from expenseManagementApp import views
from rest_framework.routers import DefaultRouter
from expenseManagementApp.views import ExpenseViewSet, UserViewSet, api_root
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns

expense_list = ExpenseViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

expense_detail = ExpenseViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
expense_highlight = ExpenseViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})


urlpatterns = [
    url(r'^$', api_root),
    url(r'^expenses/$', expense_list, name='expense-list'),
    url(r'^expenses/(?P<pk>[0-9]+)/$', expense_detail, name='expense-detail'),
    url(r'^expenses/(?P<pk>[0-9]+)/highlight/$', expense_highlight, name='expense-highlight'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/totalExpense$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail')
]
urlpatterns = format_suffix_patterns(urlpatterns)
# # Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'expenses', views.ExpenseViewSet)
# router.register(r'users', views.UserViewSet)

# # The API URLs are now determined automatically by the router.
# # Additionally, we include the login URLs for the browsable API.
# urlpatterns = [
#     url(r'^', include(router.urls)),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]
