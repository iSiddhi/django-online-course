from django.contrib import admin
from django.contrib.auth.models import User
from .models import Course, Lesson, Question, Choice, Submission, Enrollment

# Inline for choices under question
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

# Inline for questions under lesson
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

# Admin for Question (shows choices inline)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

# Admin for Lesson (shows questions inline)
class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

# Register models
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Enrollment)