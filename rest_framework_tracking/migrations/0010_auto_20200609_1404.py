# Generated by Django 3.0.6 on 2020-06-09 14:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('rest_framework_tracking', '0009_view_method_max_length_200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apirequestlog',
            name='path',
            field=models.CharField(db_index=True, help_text='url path', max_length=200),
        ),
        migrations.AlterField(
            model_name='apirequestlog',
            name='username_persistent',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='apirequestlog',
            name='view',
            field=models.CharField(blank=True, db_index=True, help_text='method called by this endpoint',
                                   max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='apirequestlog',
            name='user_agent',
            field=models.TextField(help_text='user agent of machine making the request')
        ),
        migrations.AlterField(
            model_name='apirequestlog',
            name='browser',
            field=models.CharField(max_length=200, blank=True, null=True)
        ),
        migrations.AlterField(
            model_name='apirequestlog',
            name='operating_system',
            field=models.CharField(max_length=200, blank=True, null=True)
        )
    ]
