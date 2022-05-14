import json
from django.shortcuts import render
from graph.models import Currency


def home(request):
    dataset = Currency.objects.all().order_by('base_date')
    base_date = list()
    eur = list()
    brl = list()
    jpy = list()
    for line in dataset:
        if not line.base_date.date() == base_date[:-1]:
            base_date.append(line.base_date.date())
            eur.append(float(line.eur))
            brl.append(float(line.brl))
            jpy.append(float(line.jpy))

    data = {"base_date": base_date, "eur": eur, "brl": brl, "jpy": jpy}
    return render(request, 'home.html', data)
