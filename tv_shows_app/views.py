from django.shortcuts import render, redirect
from . models import Show, ShowManager
from django.contrib import messages

# Create your views here.
def redirect_shows(request):
    return redirect("/shows")

def displayAllShows(request):
    context = {
        'all_shows':Show.objects.all()
    }
    return render(request, "display_all_shows.html", context)

def addShow(request):
    if request.method == "POST":
        errors = Show.objects.validate_data(request.POST)
        if len(errors) > 0:
            for key, errormsg in errors.items():
                messages.error(request, errormsg)
            return redirect("/shows/new")

        else:
            new_show = Show.objects.create(
            title=request.POST['title_txt'],
            network=request.POST['network_txt'],
            release_date=request.POST['release_txt'],
            desc=request.POST['desc_txt']
        )
        return redirect("/shows/"+ str(new_show.id))
    return redirect("/")


def displayNewShow(request):
    return render (request, "add_show.html")

def displayShow(request, show_id):
    context = {
        'sel_show':Show.objects.get(id=show_id)
    }
    return render (request, "display_show.html", context)

def editShow(request, show_id):
    if request.method == "POST":
        errors = Show.objects.validate_data(request.POST)
        if len(errors) > 0:
            for key, errormsg in errors.items():
                messages.error(request, errormsg)
            return redirect("/shows/" + str(show_id)+"/edit")
        else:
            sel_show=Show.objects.get(id=show_id)
            sel_show.title=request.POST['title_txt']
            sel_show.network=request.POST['network_txt']
            sel_show.release_date=request.POST['release_txt']
            sel_show.desc=request.POST['desc_txt']
            sel_show.save()
            return redirect("/shows/"+ str(sel_show.id))
    return redirect("/")


def displayEditShow (request, show_id):
    context = {
        'this_show':Show.objects.get(id=show_id)
    }
    return render (request, "edit_show.html", context)

def deleteShow(request, show_id):
    Show.objects.get(id=show_id).delete()
    return redirect('/shows')