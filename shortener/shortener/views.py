from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.shortcuts import redirect

@csrf_exempt
def store(request: HttpRequest):
    # TODO: validate
    ret = {"Status": "Error"}
    status = 400

    if request.method == "POST":
        url = request.GET.get("url")
        id = settings.URL_STORAGE.process_url(url)
        ret = {"id": id}
        status = 200

    return JsonResponse(ret, status=status)


def redirect_id(request):
    url_id = request.GET.get("id")
    target_url = settings.URL_STORAGE.get_redirect_url(url_id)
    if not target_url:
        return JsonResponse({"error": f"invalid id {url_id}"})

    return redirect(target_url)


def stats(request: HttpRequest):
    stats_result = settings.URL_STORAGE.get_statistics()

    return JsonResponse({"Statistics": stats_result})
