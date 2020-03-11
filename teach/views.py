from django.shortcuts import render
from teach.models import MathNotebook

# Create your views here.
def teach_list(request):
  notebooks = MathNotebook.objects.order_by('title')
  return render(request, 'teach/index.html', {'notebooks': notebooks})
