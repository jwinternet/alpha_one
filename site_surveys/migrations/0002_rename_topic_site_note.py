# Generated by Django 5.0.3 on 2024-03-15 22:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_surveys', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Topic',
            new_name='Site',
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_surveys.site')),
            ],
            options={
                'verbose_name_plural': 'notes',
            },
        ),
    ]