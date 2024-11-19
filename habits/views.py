from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginations import CustomPagination
from habits.serliazers import HabitSerializer


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated, )


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        """ Присваиваем создателя создаваемому объекту """
        serializer.instance.owner = self.queryset.user


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, )


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, )


class HabitDeleteAPIView(generics.DestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, )


class HabitListPublicAPIView(generics.ListAPIView):
    """ Отдает все привычки, у которых отмечено Опубликовано """
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(sing_publicity=True)
