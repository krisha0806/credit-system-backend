from django.urls import path
from .views import index, get_users,create_user,credit_entries,user_dashboard,credit_entry_detail,register_customer  

urlpatterns = [
    path('', index),
    path('users/', get_users), 
    path('users/create/', create_user),
    path('credits/', credit_entries),
    path('dashboard/<int:user_id>/', user_dashboard),
    path('credits/<int:entry_id>/', credit_entry_detail),  
    path('register/', register_customer),
]

