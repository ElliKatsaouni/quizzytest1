from quizzy.models import Quiz
import django_filters


class WeekdayFilter(django_filters.FilterSet):
    class Meta:
        model = Quiz
        fields = ['weekday']
