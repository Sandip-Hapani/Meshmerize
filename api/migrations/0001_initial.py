# Generated by Django 3.2.20 on 2023-07-18 18:44

from django.db import migrations, models
import extpack.macaddress.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60, unique=True)),
                ('macAdd', extpack.macaddress.fields.MACAddressField(blank=True, integer=True, null=True)),
                ('apiKey', models.CharField(max_length=100)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
