from django.urls import path
from . import views
	

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('finches', views.finches_index, name='index'),
    path('finch/<int:finch_id>/', views.finches_detail, name='detail'),
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
    path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name = 'add_feeding'),
    path('finches/<int:finch_id>/add_accessories/<int:accessory_id>/', views.add_accessory, name='add_accessory'),
    path('finches/<int:finch_id>/remove_accessories/<int:accessory_id>/', views.remove_accessory, name='remove_accessory'),
    path('accessories/', views.AccessoryList.as_view(), name='accessory_index'),
    path('accessories/<int:pk>/', views.AccessoryDetail.as_view(), name='accessory_detail'),
    path('accessories/create/', views.AccessoryCreate.as_view(), name='accessory_create'),
    path('accessories/<int:pk>/update/', views.AccessoryUpdate.as_view(), name='accessory_update'),
    path('accessories/<int:pk>/delete/', views.AccessoryDelete.as_view(), name='accessory_delete'),
]

