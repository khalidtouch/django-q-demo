from django.http import JsonResponse
from django_q.tasks import async_task

def index(request):
    payload = {
        "message": "Hello, world. You're at the delly index. delayed"
    }
    async_task('main.services.sleep_and_print', 20)
    return JsonResponse(payload)
