# Generated by Django 3.1.3 on 2020-12-02 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
