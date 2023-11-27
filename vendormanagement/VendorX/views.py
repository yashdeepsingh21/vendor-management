from django.http import HttpResponse
from django.shortcuts import render
from django.core.serializers import serialize
from .models import VendorModel, PurchaseOrder, PerformanceModel
import json


# Create your views here.
def create_vendor(request):
    try:
        name = request.POST.get('name')
        contact_details = request.POST.get('contact_details')
        address = request.POST.get('address')

        if name and contact_details and address:
            vendor = VendorModel(name=name, contact_details=contact_details, address=address)
            vendor.save()
            print(name, contact_details, address)
            return HttpResponse("Vendor created successfully")
        else:
            return HttpResponse("All fields are required")

    except Exception as e:
        return HttpResponse(e)


def get_vendors(request):
    try:
        vendors = VendorModel.objects.all()
        serialized_vendors = serialize('json', vendors)
        print(serialized_vendors)
        return HttpResponse(serialized_vendors)

    except Exception as e:
        return HttpResponse(e)


def specific_vendor(request, vendor_id):
    try:
        if request.method == 'GET':
            vendor = VendorModel.objects.get(vendor_code=vendor_id)
            serialized_vendor = serialize('json', [vendor])
            print(serialized_vendor)
            return HttpResponse(serialized_vendor)

        # handling Put request for same url
        elif request.method == "PUT":
            data = json.loads(request.body.decode('utf-8'))
            print(data)
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


# def update_vendor(request, vendor_id):
#     try:
#         print(type(request.method))
#         if request.method == "PUT":
#             data = json.loads(request.body.decode('utf-8'))
#             print(data)
#             vendor = VendorModel.objects.get(vendor_code=vendor_id)
#             vendor.name = data['name']
#             vendor.contact_details = data['contact_details']
#             vendor.address = data['address']
#             vendor.save()
#             return HttpResponse('put request works successfully')
#         return HttpResponse('not working')
#
#     except Exception as e:
#         return HttpResponse(e)
#
#
# def delete_vendor(request, vendor_id):
#     try:
#         if request.method == 'DELETE':
#             vendor = VendorModel.objects.get(vendor_code=vendor_id)
#             vendor.delete()
#             return HttpResponse('delete request works successfully')
#         return HttpResponse("wrong request")
#
#     except Exception as e:
#         return HttpResponse(e)