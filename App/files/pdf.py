from datetime import datetime 
import io
import csv 

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template

from xhtml2pdf import pisa

from App.models import *
from App.forms import *

def payslip(request, pk):
    # data

    company_name = "wawericom company"
    date = datetime.now()
    client_name = "simon kamau"
    product_name = "wawericom Analytics"

    payslip_data = {
        'company_name' : company_name,
        'date' : date,
        'client_name' : client_name,
        'product_name' : product_name
    }

    template = get_template('pdf/payslip.html')
    payslip_html = template.render(payslip_data)

    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = 'filename = "payslip.pdf"'

    pisa_status = pisa.CreatePDF(payslip_html, desc=response)

    if pisa_status.err:
        return HttpResponse("error generating the pdf")
    
    return response



