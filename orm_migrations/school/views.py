from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'

    result = Student.objects.all().order_by('group').prefetch_related('teacher')

    context = {
        'object_list': result
    }

    return render(request, template, context)
