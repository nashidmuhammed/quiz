# Generated by Django 4.1.3 on 2022-11-07 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grammar', '0006_alter_client_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]