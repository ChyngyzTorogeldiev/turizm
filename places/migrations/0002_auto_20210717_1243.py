# Generated by Django 3.2.5 on 2021-07-17 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['name'], 'verbose_name': 'место', 'verbose_name_plural': 'Места'},
        ),
        migrations.AlterField(
            model_name='place',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
