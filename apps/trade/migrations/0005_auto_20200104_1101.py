# Generated by Django 2.0 on 2020-01-04 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0004_auto_20200104_1039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderinfo',
            old_name='pay_status',
            new_name='trade_status',
        ),
    ]
