from django.shortcuts import render

def tmp(request):
    return render(request, "tmp.html", locals())
