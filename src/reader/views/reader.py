from django.shortcuts import render


def read(request):
    result = "temp"

    image64 = request.POST

    return render(request, "home/read_result.html", {
        'result': result
    })
