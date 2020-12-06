import os
import datetime

from django.http import request
from django.shortcuts import render
from factura.models import Receipt, LineReceipt
from django.db.models import Sum

# Create your views here.

def home(request):
    return render(request, 'factura/home.html')

def receipts(request):
    receipts = Receipt.objects.all()
    return render(request, 'factura/receipts.html', {
        "receipts": receipts.order_by("date_of_issue"),
    })

def linereceipt(request, num_receipt):
    return render(request, 'factura/linereceipt.html', {
        "receipts": Receipt.objects.get(pk=num_receipt),
    })