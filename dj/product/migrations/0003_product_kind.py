# Generated by Django 4.2.5 on 2023-09-19 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_remove_product_unit"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="kind",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]