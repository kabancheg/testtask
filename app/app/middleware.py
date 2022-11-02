from django.db import connection


class DebugQueriesMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        for q in connection.queries:
            print(q['sql'])
        return response
