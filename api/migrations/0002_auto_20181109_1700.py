# Generated by Django 2.1.3 on 2018-11-09 17:00

from django.db import migrations


def create_pizza(apps, schema_editor):
    Pizza = apps.get_model('api', 'Pizza')
    Pizza.objects.create(size='30')


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            create_pizza, reverse_code=migrations.RunPython.noop),
    ]
