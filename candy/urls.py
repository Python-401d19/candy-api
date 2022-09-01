from django.urls import path
from .views import CandyList, CandyDetail

urlpatterns = [
    path("", CandyList.as_view(), name="candy_list"),
    path("<int:pk>/", CandyDetail.as_view(), name="candy_detail"),
]
