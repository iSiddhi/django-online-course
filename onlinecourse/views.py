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

        for question in Question.objects.filter(lesson__course=course):
            selected = request.POST.get(str(question.id))

            if selected:
                choice = Choice.objects.get(id=int(selected))
                submission.choices.add(choice)

        return redirect('show_exam_result', course_id=course.id, submission_id=submission.id)


def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)

    choices = submission.choices.all()

    selected_ids = [choice.id for choice in choices]
    grade = sum(1 for c in choices if c.is_correct)
    possible = len(choices)

    return render(request, 'result.html', {
        'course': course,
        'selected_ids': selected_ids,
        'grade': grade,
        'possible': possible,
        'choices': choices
    })
