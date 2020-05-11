from django.shortcuts import render, HttpResponse
import subprocess

from .forms import AddCowsay
from .models import CowSayInput


def cowtext(string):
    cmd = ['cowsay', string]
    output = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]
    return output.decode("utf-8")


def index(request):
    html = 'index.html'
    if request.method == 'POST':
        form = AddCowsay(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            CowSayInput.objects.create(
                text=data['text']
            )
            output = cowtext(data['text'])
            form = AddCowsay()
            context = {'form': form, 'output': output}
            return render(request, html, context)

    form = AddCowsay()
    context = {'form': form}
    return render(request, html, context)


def history(request):
    html = 'history.html'
    items = list(CowSayInput.objects.all())
    items.reverse()
    posts = [cowtext(post.text) for post in items[:10]]
    context = {'items': posts}
    return render(request, html, context)
