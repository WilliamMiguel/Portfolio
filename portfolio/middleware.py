from ipware import get_client_ip
from django.shortcuts import render
from portfolio.models import Visitants


class IPIsValid():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip, private = get_client_ip(request)
        visitant = Visitants.objects.filter(visitant_ip = ip)
        visitant[0].more_visits()
        print(visitant[0].number_visits)
        if visitant[0].black_list is True:
            return render(request, 'E404.html')
        # else:
        #     return self.get_response(request)
        
        return self.get_response(request)