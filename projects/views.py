from django.shortcuts import render
from projects.models import Project

def projects_list(request):
  projects = Project.objects.all()
  return render(request, 'projects/index.html', {'projects': projects})

def project_detail(request, pk):
  project = Project.objects.get(pk=pk)
  return render(request, 'programmer/project_detail.html', {'project': project})