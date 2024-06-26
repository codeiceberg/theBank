# Generated by Django 2.1.5 on 2024-04-09 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20240408_0421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='running_balance',
        ),
        migrations.AlterField(
            model_name='account',
            name='account_balance',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_amout',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
