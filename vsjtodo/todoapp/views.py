from django.shortcuts import HttpResponse, render

from .forms import TodoForm
from .models import TodoModel

# Del

def delete(request):
    if request.POST:
        id = request.POST["id"]

        newtask = TodoModel.objects.filter(id=id)[0]
        newtask.delete()

        return HttpResponse("Deleted")

    if request.GET:
        id = request.GET["id"]
        print(id)
        data = TodoModel.objects.filter(id=id)[0]
        print(data)
        data = {'dateoftask': data.dateoftask, 'task': data.task, "description": data.description,
                "status": data.status}

        return render(request, "update.html", {"id": id, "form": TodoForm(initial=data)})

    return render(request, "update.html")


# Create your views code here.
def index(request):
    return render(request, "test.html")

def update(request):
    if request.POST:
        id = request.POST["id"]

        data = TodoForm(request.POST)
        print("Data ", data)
        newtask = TodoModel.objects.filter(id=id)[0]
        if data.is_valid():
            newtask.task = data.instance.task
            newtask.description = data.instance.description
            newtask.dateoftask = data.instance.dateoftask
            newtask.status = data.instance.status
            newtask.save()
            return HttpResponse("Updated")

    if request.GET:
        id = request.GET["id"]
        print(id)
        data = TodoModel.objects.filter(id=id)[0]
        print(data)
        data = {'dateoftask': data.dateoftask, 'task': data.task, "description": data.description,
                "status": data.status}

        return render(request, "update.html", {"id": id, "form": TodoForm(initial=data)})

    return render(request, "update.html")


def alltasks(request):
    data = TodoModel.objects.all().order_by('id').reverse()
    return render(request, "alltasks.html", {"tasks": data})


def form(request):
    if request.POST:
        newtask = TodoForm(request.POST)
        if newtask.is_valid():
            newtask.save(commit=False)
            newtask.save()
            return HttpResponse("Saved")
        return HttpResponse("Not Saved")
    return render(request, "form.html", {"form": TodoForm()})
