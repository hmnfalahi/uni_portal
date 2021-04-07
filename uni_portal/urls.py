from django.contrib import admin
from django.urls import path, include
from members import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.members_list),
    path('staff/', include('staffs.urls')),
]
