from django.shortcuts import render


# def demo(request):
#     name="india"
#
#     return render(request,"index.html",{'name':name})
# def add(request):
#     num1=request.GET["n1"]
#     num2=request.GET["n2"]
#     res=int(num1)+int(num2)
#
#     return render(request,"about.html",{"obj":res})
def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def service(request):
    return render(request, "service.html")


def packages(request):
    return render(request, "package.html")


def destination(request):
    return render(request, "destination.html")


def booking(request):
    return render(request, "booking.html")


def tavelguid(request):
    return render(request, "team.html")


def testimonial(request):
    return render(request, "testimonial.html"),


def error(request):
    return render(request, "404.html")


def contact(request):
    return render(request, "contact.html")
