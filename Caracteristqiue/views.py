from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from Caracteristqiue.models import Utilite,Pam,Avoir
from .forms import PamForm,UtiliteForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


class PamCreate(CreateView):
    model         =Pam
    form_class    =PamForm
    template_name ="Pam/CreatePam.html"
    success_url   =reverse_lazy('Pam_list')


def Pam_list(request):
    pam = Pam.objects.all()
    utilite = Utilite.objects.all()

    context = { "pam": pam,"utilite":utilite }
    return render(request, "Pam/pam_list.html", context)


@login_required()
def Pam_update(request, slug=None):
    instance = get_object_or_404(pam, slug=slug)
    if instance.user != request.user:
        raise Http404
    else:
        form = PamForm(request.POST or None, instance=instance)
        if form.is_valid():
            pam = form.save(commit=False)
            pam.user = request.user
            pam.save()
            messages.success(request, 'Pam was Updated.')
            return redirect(pam.get_absolute_url())
        context = { "form": form,
                    }
    return render(request, "Pam/CreatePam.html", context)



def pam_detail(request, slug=None):

    pams = get_object_or_404(Pam, slug=slug)
    utilite_list = Utilite.objects.filter(pams=pams)
    context = { "question": question,
                "answers_list": utilite_list,
                 }
    if request.user.is_authenticated:
        form = AnswerForm(request.POST or None)
        if form.is_valid():
            utilite = form.save(commit=False)
            utilite.user = request.user
            utilite.pams = pams
            answer.save()
            messages.success(request, 'Utilites was Posted.')
            form = UtiliteForm()    
        context = { "pams": pams,
                    "form": form,
                    "utilite_list": utilite_list,
                  }
    return render(request, "Pam/pam_detail.html", context)


@login_required()
def pam_delete(request, slug=None):
    pam = get_object_or_404(Pam, slug=slug)
    if not request.user.is_authenticated:
        raise Http404 
    else:
        if pam.user != request.user:
            raise Http404
        else:
            pam.delete() 
            messages.error(request, 'Pams was Deleted.')
            return redirect(request.user.get_absolute_url()) 

class UtiliteCreate(CreateView):
    model         =Utilite
    form_class    =UtiliteForm
    template_name ="Pam/CreateUtilite.html"
    success_url   =reverse_lazy('Utilite_list')

@login_required()
def Utilite_update(request, slug=None, pk=None):
    pam = get_object_or_404(Pam, slug=slug)
    instance = get_object_or_404(Utilite, pk=pk)
    if instance.user != request.user:
        raise Http404
    else:
        form = UtiliteForm(request.POST or None, instance=instance)
        if form.is_valid():
            utilite = form.save(commit=False)
            utilite.user = request.user
            utilite.pam = pam
            utilite.save()
            messages.success(request, 'Utilite was Updated.')
            return redirect(pam.get_absolute_url())
        context = { "form": form,
                    }
    return render(request, "Pam/CreateUtilite.html", context)


@login_required()
def Utilite_delete(request, slug=None, pk=None):
    pam = get_object_or_404(Pam, slug=slug)
    utilite = get_object_or_404(Utilite, pk=pk)
    if not request.user.is_authenticated:
        raise Http404 
    else:
        if answer.user != request.user:
            raise Http404
        else:
            answer.delete() 
            messages.error(request, 'Utilite was Deleted.')
            return redirect(pam.get_absolute_url())
