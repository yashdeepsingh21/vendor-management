from django.http import HttpResponse
from django.shortcuts import render
from django.core.serializers import serialize
from .models import VendorModel, PurchaseOrder, PerformanceModel
import json
from datetime import datetime, timedelta


# Vendors API written down below
def vendors(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            contact_details = request.POST.get('contact_details')
            address = request.POST.get('address')

            if name and contact_details and address:
                vendor = VendorModel(name=name, contact_details=contact_details, address=address)
                vendor.save()
                return HttpResponse("Vendor created successfully")
            else:
                return HttpResponse("All fields are required")
        elif request.method == "GET":
            vendors = VendorModel.objects.all()
            serialized_vendors = serialize('json', vendors)
            return HttpResponse(serialized_vendors)
        else:
            return HttpResponse("Method not allowed")
    except Exception as e:
        return HttpResponse(e)


def specific_vendor(request, vendor_id):
    try:
        if request.method == 'GET':
            vendor = VendorModel.objects.get(vendor_code=vendor_id)
            serialized_vendor = serialize('json', [vendor])
            return HttpResponse(serialized_vendor)

        # handling Put request for same url
        elif request.method == "PUT":
            data = json.loads(request.body.decode('utf-8'))
            vendor = VendorModel.objects.get(vendor_code=vendor_id)
            vendor.name = data['name']
            vendor.contact_details = data['contact_details']
            vendor.address = data['address']
            vendor.save()
            return HttpResponse('put request works successfully')

        # handling DELETE request for same url
        elif request.method == 'DELETE':
            vendor = VendorModel.objects.get(vendor_code=vendor_id)
            vendor.delete()
            return HttpResponse('delete request works successfully')

    except Exception as e:
        return HttpResponse(e)


# Purchase order API written down below

def purchase_order(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))
            vendor = data['vendor']
            items = data['items']
            order_date = datetime.now()
            delivery_date = order_date + timedelta(days=7)
            quantity = data["quantity"]
            status = "pending"
            issue_date = order_date + timedelta(days=1)
            if items and vendor and quantity:
                vm = VendorModel.objects.get(vendor_code=vendor)
                po = PurchaseOrder(vendor=vm, order_date=order_date,
                                   delivery_date=delivery_date, items=items, quantity=int(quantity), status=status,
                                   issue_date=issue_date)
                po.save()
                return HttpResponse(
                    f"your order number has been placed and {delivery_date} is the expected delivery date")
        elif request.method == 'GET':
            po = PurchaseOrder.objects.all()
            serialized_po = serialize('json', po)
            return HttpResponse(serialized_po)
        return HttpResponse("unable to get data")


    except Exception as e:
        return HttpResponse(e)


def specific_purchase_order(request, po_number):
    try:
        po_number = po_number
        print(po_number)
        if request.method == 'GET':
            po = PurchaseOrder.objects.filter(po_number=po_number)
            serialized_po = serialize('json', po)
            return HttpResponse(serialized_po)

        elif request.method == 'PUT':
            data = json.loads(request.body.decode('utf-8'))
            po = PurchaseOrder.objects.get(po_number=po_number)
            po.items = data['items']
            po.quantity = data.get('quantity',)
            if po.items and po.quantity:
                po.save()
                return HttpResponse('product details updated successfully')
            return HttpResponse("product not update or found")

        elif request.method == 'DELETE':
            po = PurchaseOrder.objects.get(po_number=po_number)
            po.delete()
            return HttpResponse('Product deleted successfully')
        return HttpResponse("unable to get data")

    except Exception as e:
        return HttpResponse(e)