from quiz.models import Subject

def sorted_subjects(request):
    return {'subjects': Subject.objects.all()}