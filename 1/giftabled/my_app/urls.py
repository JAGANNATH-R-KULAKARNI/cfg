from django.urls import path
from . import views

urlpatterns=[
    path('',views.home_page,name='home_page'),
    path('login',views.login_page,name='login_page'),
    path('signup',views.signup_page,name='signup_page'),
      path('logout',views.log_out,name='logout_page'),
      path('forgot',views.forgot_password,name='forgot_password'),
      path('reset',views.change_password,name='change_passwd')
]