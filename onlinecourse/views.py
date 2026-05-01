from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Question, Choice, Enrollment, Submission

def show_exam(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    questions = Question.objects.filter(lesson__course=course)

    return render(request, 'exam.html', {
        'questions': questions,
        'course': course
    })


def submit(request, course_id):
    if request.method == 'POST':
        course = get_object_or_404(Course, pk=course_id)
        enrollment = Enrollment.objects.first()

        submission = Submission.objects.create(enrollment=enrollment)

        for key, value in request.POST.items():
            if key.isdigit():
                choice = Choice.objects.get(id=int(value))
                submission.choices.add(choice)

        return redirect('show_exam_result', course_id=course.id, submission_id=submission.id)


def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)

    selected_ids = [choice.id for choice in submission.choices.all()]
    questions = Question.objects.filter(lesson__course=course)

    total_score = 0
    possible_score = 0

    for question in questions:
        possible_score += question.grade
        if question.is_get_score(selected_ids):
            total_score += question.grade

    return render(request, 'result.html', {
        'course': course,
        'selected_ids': selected_ids,
        'grade': total_score,
        'possible': possible_score
    })
