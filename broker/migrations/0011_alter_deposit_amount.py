# Generated by Django 4.2.7 on 2024-05-03 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0010_payment_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='amount',
            field=models.IntegerField(null=True),
        ),
    ]