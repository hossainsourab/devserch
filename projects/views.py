from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Project, Tag, Review
from .forms import ProjectForm

# Create your views here.

""""
projectsList = [

    {
        'id': '1',
        'title': 'Ecommerce website',
        'description': 'Fully functional ecommerce website',
    },
    {
        'id': '2',
        'title': 'Portfolio website',
        'description': 'This was a project where i built out my portfolio',
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'Awesomely source project i am still working on',
    }

]



def projects(request):
    pages = "Projects"
    number = 10
    contex = {'pages': pages, 'number': number, 'projects': projectsList}
    return render(request, 'projects/projects.html', contex)


def project(request, pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/singel-project.html', {'project': projectObj})

"""


def projects(request):
    projects = Project.objects.all()
    contex = {'projects': projects}
    return render(request, 'projects/projects.html', contex)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()

    return render(request, 'projects/singel-project.html', {'project': projectObj, 'tags': tags})


@login_required(login_url='login')
def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    contex = {'form': form}
    return render(request, 'projects/project_form.html', contex)


@login_required(login_url='login')
def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('/')

    contex = {'form': form}
    return render(request, 'projects/project_form.html', contex)


@login_required(login_url='login')
def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect('/')
    context = {'object': project}
    return render(request, 'projects/delete_template.html', context)
