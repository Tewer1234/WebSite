# Generated by Django 4.0.6 on 2022-09-18 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_tool', '0008_mrnatbl_delete_genetbl_delete_genetbl2'),
    ]

    operations = [
        migrations.CreateModel(
            name='NcrnaTbl',
            fields=[
                ('geneid', models.TextField(blank=True, db_column='GeneID', primary_key=True, serialize=False)),
                ('types', models.TextField(blank=True, db_column='Types', null=True)),
                ('transcript', models.TextField(blank=True, db_column='Transcript', null=True)),
            ],
            options={
                'db_table': 'ncRNA_TBL',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dicty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='KeyVal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=200)),
                ('value', models.CharField(db_index=True, max_length=200)),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_tool.dicty')),
            ],
        ),
    ]
