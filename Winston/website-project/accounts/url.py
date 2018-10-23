from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
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
    path('test2', views.test2, name='test2'),
    path('delete/<id>', views.delete, name='delete'),
    path('edit/<id>', views.edit, name='edit'),
    path('loadnew', views.loadnew, name='loadnew'),
    path('addcars', views.addcars, name='addcars'),
    path('viewcars', views.viewcars, name='viewcars'),
    path('viewmore/<id>', views.viewmore, name='viewmore'),
    path('audi_viewmore/<id>', views.audi_viewmore, name='audi_viewmore'),
    path('kia_viewmore/<id>', views.kia_viewmore, name='kia_viewmore'),
    path('hyundai_viewmore/<id>', views.hyundai_viewmore, name='hyundai_viewmore'),
    path('mitsubishi_viewmore/<id>', views.mitsubishi_viewmore, name='mitsubishi_viewmore'),
    path('toyota_viewmore/<id>', views.toyota_viewmore, name='toyota_viewmore'),
    path('view_audi', views.view_audi, name='view_audi'),
    path('view_kia', views.view_kia, name='view_kia'),
    path('view_toyota', views.view_toyota, name='view_toyota'),
    path('view_mitsubishi', views.view_mitsubishi, name='view_mitsubishi'),
    path('view_hyundai', views.view_hyundai, name='view_hyundai'),
    path('show_most_rent', views.show_most_rent, name='show_most_rent'),
    path('show_city_orders', views.show_city_orders, name='show_city_orders'),
    path('show_month_orders', views.show_month_orders, name='show_month_orders'),
    path('show_month_orders_2006', views.show_month_orders_2006, name='show_month_orders_2006'),
    path('show_month_orders_2007', views.show_month_orders_2007, name='show_month_orders_2007'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


