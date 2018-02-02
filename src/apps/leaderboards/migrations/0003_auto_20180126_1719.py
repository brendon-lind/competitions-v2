# Generated by Django 2.0.1 on 2018-01-26 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboards', '0002_auto_20180125_0344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='column',
            name='computation_columns',
        ),
        migrations.RemoveField(
            model_name='leaderboard',
            name='primary_column',
        ),
        migrations.AddField(
            model_name='column',
            name='computation_indexes',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='leaderboard',
            name='primary_index',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='column',
            name='computation',
            field=models.TextField(blank=True, choices=[('avg', 'Average')], null=True),
        ),
        migrations.AlterField(
            model_name='column',
            name='sorting',
            field=models.TextField(choices=[('desc', 'Descending'), ('asc', 'Ascending')], default='desc'),
        ),
        migrations.AlterField(
            model_name='leaderboard',
            name='competition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leaderboards', to='competitions.Competition'),
        ),
    ]