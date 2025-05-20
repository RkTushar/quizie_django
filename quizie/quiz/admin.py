from django.contrib import admin
from .models import Category, Quiz, Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('text', 'quiz')

class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')

admin.site.register(Category)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
