# Generated by Django 3.0.4 on 2020-06-18 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200617_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='banner_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]