# Generated by Django 2.1.11 on 2019-11-22 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0003_data_file_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
