from ipware import get_client_ip
from django.shortcuts import render
from portfolio.models import User

BLACK_LIST = [
    '127.0.0.2'
]

class IPIsValid():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip, private = get_client_ip(request)

        if ip in BLACK_LIST:
            return render(request, 'E404.html')
        else:
            return self.get_response(request)