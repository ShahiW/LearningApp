from quiz.models import Subject

def sorted_subjects(request):
    sorted_subjects = {s.name: s for s in sorted(Subject.objects.all(), key=lambda el: el.name)}
    return {'subjects': sorted_subjects}