# Generated by Django 2.1.2 on 2019-01-16 19:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0005_auto_20181002_2045'),
        ('competitions', '0022_auto_20181008_2114'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompetitionDump',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.TextField(blank=True, choices=[('Starting', 'None'), ('Finished', 'Finished'), ('Failed', 'Failed')], null=True)),
                ('details', models.TextField(blank=True, null=True)),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dumps', to='competitions.Competition')),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competition_dump_file', to='datasets.Data')),
            ],
        ),
        migrations.AlterField(
            model_name='submission',
            name='secret',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='submission',
            name='status',
            field=models.CharField(choices=[('None', 'None'), ('Submitting', 'Submitting'), ('Submitted', 'Submitted'), ('Preparing', 'Preparing'), ('Running', 'Running'), ('Cancelled', 'Cancelled'), ('Finished', 'Finished'), ('Failed', 'Failed')], default='None', max_length=128),
        ),
        migrations.AlterField(
            model_name='submissiondetails',
            name='submission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='details', to='competitions.Submission'),
        ),
    ]