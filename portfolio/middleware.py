from ipware import get_client_ip
from django.shortcuts import render
from portfolio.models import Visitants
from django.db.models import F


class IPIsValid():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip, private = get_client_ip(request)
        visitant = Visitants.objects.filter(visitant_ip = ip).exists()
        if visitant is False:
            visitant = Visitants.objects.create(visitant_ip = ip)

        visitant = Visitants.objects.filter(visitant_ip = ip)

        Visitants.objects.update(number_visits = F('number_visits') + 1)
        
        if visitant[0].black_list is True:
            return render(request, 'E404.html')
        else:
            return self.get_response(request)
        # return self.get_response(request)