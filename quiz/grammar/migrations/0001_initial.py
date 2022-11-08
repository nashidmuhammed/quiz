# Generated by Django 4.1.3 on 2022-11-07 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qst', models.CharField(max_length=200)),
                ('no', models.IntegerField(unique=True)),
                ('a', models.CharField(max_length=100)),
                ('b', models.CharField(max_length=100)),
                ('c', models.CharField(max_length=100)),
                ('d', models.CharField(max_length=100)),
                ('ans', models.CharField(max_length=100)),
                ('time', models.IntegerField(default=90)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(default=0)),
                ('no', models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.SET_NULL, to='grammar.questions')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]