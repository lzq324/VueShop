# Generated by Django 2.0 on 2020-01-04 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0005_auto_20200104_1101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderinfo',
            old_name='trade_status',
            new_name='pay_status',
        ),
    ]
