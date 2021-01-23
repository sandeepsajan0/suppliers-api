# Generated by Django 3.1.5 on 2021-01-21 04:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('primary_full_name', models.CharField(blank=True, max_length=250, null=True)),
                ('primary_email', models.EmailField(max_length=254, unique=True)),
                ('primary_phone', models.CharField(blank=True, max_length=10, null=True)),
                ('secondary_full_name', models.CharField(blank=True, max_length=250, null=True)),
                ('secondary_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('secondary_phone', models.CharField(blank=True, max_length=10, null=True)),
                ('related_entities', models.TextField(blank=True, null=True)),
                ('active_status', models.BooleanField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('auth_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('active_status', models.BooleanField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_supplier', to='suppliers.supplier')),
            ],
        ),
    ]