from django.shortcuts import render
from teach.models import MathNotebook

# Create your views here.
def teach_list(request):
  notebooks = MathNotebook.objects.all()
  return render(request, 'teach/index.html', {'notebooks': notebooks})
