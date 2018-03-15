from django.contrib import admin
from quizzy.models import UserProfile, City, Pub, Quiz


class QuizAdmin(admin.ModelAdmin):
    list_display = ('weekday', 'pub', 'upVotes', 'downVotes')


class PubAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')


admin.site.register(UserProfile)
admin.site.register(City)
admin.site.register(Pub, PubAdmin)
admin.site.register(Quiz, QuizAdmin)
