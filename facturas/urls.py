import datetime
import os

from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url

import factura.views

urlpatterns = [
    path('', factura.views.home),
    path('admin/', admin.site.urls),
    path('linereceipt/<int:num_receipt>', factura.views.linereceipt),
    path('receipts', factura.views.receipts),
]