from django.urls import path
from . import views

urlpatterns = [
    path('', views.endpoints),
    path('advocates/', views.advocate_list),
    # path('advocates/<int:id>/', views.advocate_detail)
    path('advocates/<int:id>/', views.AdvocateDetail.as_view())
]
