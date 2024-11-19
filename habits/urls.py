from django.urls import path
from rest_framework.permissions import AllowAny

from habits.apps import HabitsConfig
from habits.views import HabitListAPIView, HabitCreateAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, \
    HabitDeleteAPIView, HabitListPublicAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('list/', HabitListAPIView.as_view(), name='habit-list'),
    path('list-publiс/', HabitListPublicAPIView.as_view(permission_classes=(AllowAny, )), name='habit-list-public'),
    path('create/', HabitCreateAPIView.as_view(), name='habit-create'),
    path('<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit-get'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit-update'),
    path('delete/<int:pk>/', HabitDeleteAPIView.as_view(), name='habit-delete'),
]