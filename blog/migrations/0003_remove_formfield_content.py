# Generated by Django 2.0.4 on 2018-04-18 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_formfield_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formfield',
            name='content',
        ),
    ]
