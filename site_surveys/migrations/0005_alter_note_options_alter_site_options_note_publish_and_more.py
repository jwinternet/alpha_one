# Generated by Django 5.0.3 on 2024-03-16 22:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_surveys', '0004_site_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['-publish'], 'verbose_name_plural': 'notes'},
        ),
        migrations.AlterModelOptions(
            name='site',
            options={'ordering': ['-publish'], 'verbose_name_plural': 'sites'},
        ),
        migrations.AddField(
            model_name='note',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='note',
            name='slug',
            field=models.SlugField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='site',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='site',
            name='slug',
            field=models.SlugField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
