import json
from django.shortcuts import render
from graph.models import Currency


def home(request):
    dataset = Currency.objects.all().order_by('base_date')
    # currency = {}
    # for line in dataset:
    #     currency[f"{str(line.base_date.date())}"] = {
    #         "eur": str(line.eur),
    #         "brl": str(line.brl),
    #         "jpy": str(line.jpy),
    #     }

    base_date = list()
    eur = list()
    brl = list()
    jpy = list()
    for line in dataset:
        base_date.append(line.base_date.date())
        eur.append(float(line.eur))
        brl.append(float(line.brl))
        jpy.append(float(line.jpy))

    data = {"base_date": base_date, "eur": eur, "brl": brl, "jpy": jpy}
    return render(request, 'home.html', data)
