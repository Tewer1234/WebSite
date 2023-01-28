# Generated by Django 4.0.6 on 2022-08-17 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gene',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gene_id', models.CharField(max_length=100)),
                ('transcript_id', models.CharField(max_length=100)),
                ('numbers', models.IntegerField()),
            ],
        ),
    ]
