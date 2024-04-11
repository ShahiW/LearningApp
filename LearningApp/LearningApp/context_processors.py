from quiz.models import Subject

def show_subjects(request):
    return {"subjects": Subject.objects.all()}