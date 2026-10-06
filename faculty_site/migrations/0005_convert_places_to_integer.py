import re

from django.db import migrations,models

def places_to_int(apps, schema_editor):
    ExchangeProgram = apps.get_model('faculty_site', 'ExchangeProgram')
    for prog in ExchangeProgram.objects.all():
        match = re.search(r'\d+', prog.places_old)
        prog.places = int(match.group()) if match else 0
        prog.save(update_fields=['places'])

def places_to_text(apps, schema_editor):
    ExchangeProgram = apps.get_model('faculty_site', 'ExchangeProgram')
    for prog in ExchangeProgram.objects.all():
        prog.places_old = str(prog.places)
        prog.save(update_fields=['places_old'])


class Migration(migrations.Migration):

    dependencies = [
        ('faculty_site', '0004_split_university_and_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exchangeprogram',
            old_name='places',
            new_name='places_old',
        ),
        migrations.AddField(
            model_name='exchangeprogram',
            name='places',
            field=models.IntegerField(default=0, verbose_name='Кількість місць'),
            preserve_default=False,
        ),
        migrations.RunPython(places_to_int, reverse_code=places_to_text),
        migrations.AlterField(
            model_name='exchangeprogram',
            name='places_old',
            field=models.TextField(default='', verbose_name='Кількість місць'),
        ),
        migrations.RemoveField(
            model_name='exchangeprogram',
            name='places_old',
        ),
    ]
