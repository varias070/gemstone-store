import csv
import io

from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Sum, F
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from django.core.exceptions import BadRequest, ValidationError
from django.views.decorators.csrf import csrf_exempt

from .models import Deal


@csrf_exempt
def add_deal(request):
    if request.headers.get('Content-Type') != 'text/csv':
        raise ValidationError("request.headers Content-Type must text/csv")

    if request.method != 'POST':
        raise BadRequest("request method must POST")

    csv_file = io.StringIO(request.body.decode('utf-8'))
    deals = csv.DictReader(csv_file)

    headers = deals.fieldnames
    if headers != ['customer', 'item', 'total', 'quantity', 'date']:
        raise BadRequest(
            f'Заголовок csv должен быть: '
            f'customer, item, total, quantity, date. '
            f'В запросе: {headers}'
        )

    for deal in deals:
        Deal.objects.create(
            customer=deal['customer'],
            item=deal['item'],
            total=deal['total'],
            quantity=deal['quantity'],
            date=deal['date'],
        ).save()

    return HttpResponse('')


def find_top_five_clients(request):

    if request.method != 'GET':
        raise BadRequest("request method must GET")

    values = []
    top_five = Deal.objects.values('customer') \
                   .annotate(spent_money=Sum('total'), gems=ArrayAgg('item', distinct=True)) \
                   .order_by('spent_money') \
                   .reverse()[:5]
    for top in top_five:
        values.append({'username': top['customer'],
                       'spent_money': top['spent_money'],
                       'gems': top['gems']
                       })

    response = {'response': values}

    Deal.objects.all().delete()
    return JsonResponse(response)
