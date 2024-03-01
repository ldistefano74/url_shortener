from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.shortcuts import render, redirect

@csrf_exempt
def store(request: HttpRequest):
    # TODO: validate
    ret = {"Status":"Error"}
    status = 400

    if request.method == "POST":
        url = request.GET.get("url")
        id = settings.URL_STORAGE.process_url(url)
        ret = {"id": id}
        status = 200

    return JsonResponse(ret, status=status)


def redirect_id(request):
    id = request.GET.get("id")
    target_url = settings.URL_STORAGE.get_redirect_url(id)
    if not target_url:
        return JsonResponse({"error": f"invalid id {id}"})

    return redirect(target_url)


def stats(request: HttpRequest):
    stats = settings.URL_STORAGE.get_statistics()

    return JsonResponse({"Statistics": stats})
