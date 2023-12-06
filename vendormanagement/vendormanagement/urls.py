"""
URL configuration for vendormanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from VendorX.views import vendors, specific_vendor, purchase_order, specific_purchase_order,\
    acknowledgement, on_time_delivery_rate


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/vendors/', vendors),
    path('api/vendors/<int:vendor_id>/', specific_vendor),
    path('api/purchase_order/', purchase_order),
    path('api/purchase_order/<int:po_number>/', specific_purchase_order),
    path('api/purchase_orders/<int:po_id>/acknowledge/', acknowledgement),
    path('api/on_time/', on_time_delivery_rate),
]
