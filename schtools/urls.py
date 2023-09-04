# cal/urls.py
from django.urls import path
from . import views
import django.http


urlpatterns = [
path('tools/', views.tools_view, name="Tools"),
path('tools/delete/<int:id>', views.delete_cart_view, name='delete-from-cart'),
path('tools/select', views.select_view, name='select-from-cart'),
path('tools/create', views.create_schedule_view, name='create-schedule'),
path('tools/remove/<int:id>', views.remove_class_view, name='remove-from-schedule'),
path('tools/add', views.add_class_view, name='add-to-schedule'),
path('tools/toggle-send/<int:id>', views.toggle_share_schedule_view, name='toggle-send-schedule'),
path('tools/delete-schedule/<int:id>', views.delete_schedule_view, name='delete-schedule'),
path('tools/approve/<int:id>', views.advisor_approve, name='advisor-approve'),
path('tools/reject/<int:id>', views.advisor_reject, name='advisor-reject')
]
