# Generated by Django 2.0.3 on 2021-02-03 10:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_classes_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='lastmod',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]