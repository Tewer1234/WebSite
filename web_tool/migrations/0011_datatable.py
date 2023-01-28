# Generated by Django 4.0.6 on 2022-09-30 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_tool', '0010_remove_keyval_container_delete_ncrnatbl_delete_dicty_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datatable',
            fields=[
                ('geneid', models.TextField(blank=True, db_column='GeneID', primary_key=True, serialize=False)),
                ('status', models.TextField(blank=True, db_column='Status', null=True)),
                ('sequence', models.TextField(blank=True, db_column='Sequence', null=True)),
                ('genename', models.TextField(blank=True, db_column='GeneName', null=True)),
                ('othername', models.TextField(blank=True, db_column='OtherName', null=True)),
            ],
            options={
                'db_table': 'dataTable',
                'managed': False,
            },
        ),
    ]
