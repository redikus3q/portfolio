from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import util
from django import forms
from markdown2 import Markdown
import markdown2
import random

class NewTaskForm(forms.Form):
    title = forms.CharField(label="Title", widget=forms.TextInput(attrs={'class' : 'form-control col-md-8 col-lg-8'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control col-md-8 col-lg-8'}), label="New thread")
    edit = forms.BooleanField(initial=False, widget=forms.HiddenInput(), required=False)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def default(request, wiki):
    ok=0
    for i in util.list_entries():
        if i.capitalize()==wiki.capitalize():
            title=i
            ok=1
    if ok==1:
        return render(request, "encyclopedia/ofo.html", {
            "code":markdown2.markdown(util.get_entry(wiki)),
            "title":title
        })
    else:
        return HttpResponse("Page not found.")

def search(request):
    value = request.GET.get('q','')
    if(util.get_entry(value) is not None):
        return HttpResponseRedirect(reverse("default", kwargs={'wiki': value }))
    else:
        subStringEntries = []
        for entry in util.list_entries():
            if value.upper() in entry.upper():
                subStringEntries.append(entry)

        return render(request, "encyclopedia/index.html", {
        "entries": subStringEntries,
        "search": True,
        "value": value
    })

def new(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            entry = form.cleaned_data["text"]
            title= form.cleaned_data["title"]
            if(util.get_entry(title) is None or form.cleaned_data["edit"] is True):
                util.save_entry(title,entry)
                return HttpResponseRedirect(reverse("default", kwargs={'wiki': title}))
            else:
                return render(request, "encyclopedia/new.html", {
                "form": form,
                "existing": True,
                "wiki": title
                })
        else:
            return render(request, "encyclopedia/new.html",{
                "form": form,
                "existing": False
            })
    else:
        return render(request,"encyclopedia/new.html", {
            "form": NewTaskForm(),
            "existing": False
        })  

def randy(request):
    entries = util.list_entries()
    y=random.randint(0, len(entries)-1)
    return render(request, "encyclopedia/ofo.html", {
        "code":markdown2.markdown(util.get_entry(entries[y])),
        "title":entries[y]
    })

def edit(request, entry):
    entryPage = util.get_entry(entry)
    form = NewTaskForm()
    form.fields["title"].initial = entry
    form.fields["text"].initial = entryPage
    form.fields["edit"].initial = True
    return render(request, "encyclopedia/new.html", {
        "form": form,
        "edit": form.fields["edit"].initial,
        "title": form.fields["title"].initial
    })  