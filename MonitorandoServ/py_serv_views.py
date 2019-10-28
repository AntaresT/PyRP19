from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.utils import formats
from .models import Report
import json


def home(request, template="home.html"):
    reports = Report.objects.all().order_by('created')

    last_repo = reports.last()
    print(last_repo)

    total_value = {
        'd': [r.total_value for r in reports],
        'c': [formats.date_format(r.created, "SHORT_DATETIME_FORMAT") for r in reports]
    }

    return render(request, template, {'total_value': json.dumps(total_value),
                                      'last_repo': last_repo})


@api_view(['POST'])
def reports(request):
    if request.method == "POST":
        print(request.POST)
        data = {
            'name': request.data.get('name'),
            'total_value': int(request.data.get('total_value')),
            'disk_usage': float(request.data.get('disk_usage')),
            'latency': float(request.data.get('latency')),
        }
        report = Report.objects.create(**data)
        print(report)
    return JsonResponse({"message": "Your response"})
