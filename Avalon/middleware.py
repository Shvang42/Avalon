from django.utils.timezone import now
from .models import SessionInfo

class SessionInfoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        session_key = request.session.session_key
        username = request.session.get('username', 'Unknown')
        SessionInfo.objects.update_or_create(session_key=session_key, defaults={'username': username, 'last_seen': now()})
        return response
