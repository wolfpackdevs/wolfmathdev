from django.shortcuts import render

# Create your views here.
def teach_list(request):
  return render(request, 'teach/index.html')
