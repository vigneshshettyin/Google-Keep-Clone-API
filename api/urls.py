from django.urls import path
from .views import TestAPIView, CheckListsAPIView, CheckListAPIView, CheckListItemsAPIView, CheckListItemAPIView

urlpatterns = [
    path('', TestAPIView.as_view()),
    path('checklist/', CheckListsAPIView.as_view()),
    path('checklist/<int:pk>/', CheckListAPIView.as_view()),
    path('checklist/item/', CheckListItemsAPIView.as_view()),
    path('checklist/item/<int:pk>/', CheckListItemAPIView.as_view()),
]
