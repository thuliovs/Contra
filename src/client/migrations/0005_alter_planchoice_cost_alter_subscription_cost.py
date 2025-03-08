# Generated by Django 5.1.5 on 2025-03-08 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_rename_plan_planchoice_plan_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planchoice',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Plan cost'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Cost'),
        ),
    ]
