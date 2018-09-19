from django.urls import path, include
from . import views

urlpatterns = [
    path('signup',views.signup, name='signup'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('customer',views.customer, name='customer'),
    path('manager',views.manager, name='manager'),
    path('portfolio',views.portfolio, name='portfolio'),
    path('browser', views.browser, name='browser'),
    path('record', views.record, name='record'),
    path('history', views.history, name='history'),
    path('test', views.test, name='test'),
]
