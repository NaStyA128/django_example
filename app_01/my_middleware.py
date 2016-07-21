from datetime import datetime
from django.http import HttpResponse


class MiddleWare:

    def process_request(self, request):
        request.now = datetime.now()

    """
    def process_exception(self, request, exception):
        return HttpResponse('Error')
    """

    """
    def process_response(self, request, response):
        return HttpResponse('Response')
    """
