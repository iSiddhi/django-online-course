from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=200)

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    grade = models.IntegerField(default=1)   # IMPORTANT

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def is_get_score(self, selected_ids):
        correct_choices = self.choice_set.filter(is_correct=True).values_list('id', flat=True)
        return set(correct_choices) == set(selected_ids)

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Submission(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)

    def __str__(self):
        return f"{self.enrollment.user.username} submission"

# REQUIRED
class Instructor(models.Model):
    name = models.CharField(max_length=200)

class Learner(models.Model):
    name = models.CharField(max_length=200)
