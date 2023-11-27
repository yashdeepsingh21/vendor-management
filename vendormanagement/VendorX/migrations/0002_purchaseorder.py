# Generated by Django 4.2.7 on 2023-11-26 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VendorX', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('po_number', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField(blank=True, null=True)),
                ('delivery_date', models.DateTimeField(blank=True, null=True)),
                ('items', models.JSONField()),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(max_length=200)),
                ('quality_rating', models.FloatField(null=True)),
                ('issue_date', models.DateTimeField(blank=True, null=True)),
                ('acknowledgment_date', models.DateTimeField(blank=True, null=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VendorX.vendormodel')),
            ],
        ),
    ]
