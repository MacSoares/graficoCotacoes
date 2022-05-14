import json
from django.shortcuts import render
from graph.models import Currency


def home(request):
    dataset = Currency.objects.all().order_by('base_date')
    eur = list()
    base_date = list()
    jpy = list()
    brl = list()

    for line in dataset:
        eur.append(line.eur)
        base_date.append(line.base_date.date())
        jpy.append(line.jpy)
        brl.append(line.brl)

    return render(request, 'home.html', {
        'eur': eur,
        'brl': brl,
        'jpy': jpy,
        'base_date': base_date,
    })
