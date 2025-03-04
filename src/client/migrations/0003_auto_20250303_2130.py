# Generated by Django 5.1.5 on 2025-03-03 21:30

from django.db import migrations


def populate_plan_choice(apps, schema_editor):
    PlanChoice = apps.get_model('client', 'PlanChoice')
    PlanChoice.objects.create(
        plan = 'ST',
        name = 'Standard',
        cost = '3.00',
        is_active = True,
        description1 = 'Get access to standard articles and reports',
        description2 = 'Limited access',
        external_plan_id = 'P-5UX16656YT4375159M7A5AKA',
        external_api_url = 'https://www.paypal.com/sdk/js?client-id=AVNwDSxo5q4bqB-Cv8EgeewqLuC_J1KbjCwT6qj0X4_1NDvovQVBbhOTOlCDddaoGbotcN2EoVJLHlL0&vault=true&intent=subscription',
        external_style_json = """{
            "shape": "pill",
            "color": "silver",
            "layout": "vertical",
            "label": "subscribe"
        }"""
    )

    PlanChoice.objects.create(
        plan = 'PR',
        name = 'Premium',
        cost = '9.99',
        is_active = True,
        description1 = 'Get access to premium articles and reports',
        description2 = 'Unlimited access',
        external_plan_id = 'P-0S100621MM6805235M7A6KVI',
        external_api_url = 'https://www.paypal.com/sdk/js?vault=true&intent=subscription',
        external_style_json = """{
            "shape": "pill",
            "color": "gold",
            "layout": "vertical",
            "label": "subscribe"
        }"""
    )


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_planchoice_alter_subscription_cost'),
    ]

    operations = [
        migrations.RunPython(populate_plan_choice),
    ]
