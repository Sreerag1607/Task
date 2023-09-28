from . import views
from django.urls import path
from .views import BranchView, get_filtered_branches

app_name='bankapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('register', views.reg, name='reg'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('form', views.form, name='form'),
    path('new', views.simple, name='simple'),
    path('select-branch/', BranchView.as_view(), name='select_branch'),
    path('get-branches/', get_filtered_branches, name='get_filtered_branches'),
]
