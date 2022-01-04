from django.shortcuts import render

from commodity.models import CommodityInfos

def tmp(request):
    poll = CommodityInfos.objects.order_by('-sold').all()[2].price
    poll2 = 200
    poll3 = 300
    return render(request, "tmp.html", locals())
