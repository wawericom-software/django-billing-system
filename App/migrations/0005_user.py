# Generated by Django 4.2.7 on 2023-12-13 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_remove_order_refund_granted_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password1', models.CharField(max_length=255)),
                ('password2', models.CharField(max_length=255)),
            ],
        ),
    ]
