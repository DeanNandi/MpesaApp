from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_transactions),
    path('transactions/', views.display_transactions, name='display_transactions'),
    path('accesstoken/', views.get_access_token, name='get_access_token'),
    path('initiate/', views.initiate_stk_push, name='initiate_stk_push'),
    path('query/', views.query_stk_status, name='query_stk_status'),
    path('callback/', views.process_stk_callback, name='process_stk_callback'),

]
