# Generated by Django 4.2.1 on 2023-08-29 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='method',
            field=models.CharField(blank=True, choices=[('plan', 'plan'), ('fixed', 'fixed')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='package',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.packages'),
        ),
    ]
