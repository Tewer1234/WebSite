# Generated by Django 4.0.6 on 2022-08-19 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_tool', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('invented', models.IntegerField()),
                ('popularity', models.FloatField()),
            ],
        ),
    ]
