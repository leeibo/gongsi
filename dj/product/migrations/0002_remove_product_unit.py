# Generated by Django 4.2.5 on 2023-09-19 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="product", name="unit",),
    ]