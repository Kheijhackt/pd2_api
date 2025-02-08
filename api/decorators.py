from django.conf import settings
from django.http import JsonResponse
from functools import wraps

def require_api_key(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        api_key = request.GET.get("api_key")  # Get API key from URL
        if api_key != settings.API_SECRET_KEY:
            return JsonResponse({"error": "Invalid API key"}, status=403)
        return view_func(request, *args, **kwargs)
    
    return wrapped_view