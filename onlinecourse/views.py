from django.shortcuts import render
from .models import Question, Choice, Submission

# 1. EXAM PAGE
def exam(request):
    questions = Question.objects.all()
    return render(request, 'exam.html', {'questions': questions})


# 2. SUBMIT FUNCTION
def submit(request):
    if request.method == "POST":
        submission = Submission.objects.create(user=request.user)

        correct = 0
        total = 0

        for key in request.POST:
            if key.startswith("question_"):
                choice_id = request.POST.get(key)
                choice = Choice.objects.get(id=choice_id)
                submission.choices.add(choice)

                total += 1
                if choice.is_correct:
                    correct += 1

        score = (correct / total) * 100 if total > 0 else 0

        return render(request, 'result.html', {
            'score': score,
            'correct': correct,
            'total': total
        })


# 3. RESULT FUNCTION (THIS WAS MISSING ❗)
def show_exam_result(request, submission_id):
    submission = Submission.objects.get(id=submission_id)

    correct = 0
    total = submission.choices.count()

    for choice in submission.choices.all():
        if choice.is_correct:
            correct += 1

    score = (correct / total) * 100 if total > 0 else 0

    return render(request, 'result.html', {
        'score': score,
        'correct': correct,
        'total': total
    })