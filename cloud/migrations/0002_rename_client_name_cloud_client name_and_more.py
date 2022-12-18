# Generated by Django 4.0.3 on 2022-12-17 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cloud',
            old_name='client_name',
            new_name='Client Name',
        ),
        migrations.RenameField(
            model_name='cloud',
            old_name='contact_email_1',
            new_name='Contact email 1',
        ),
        migrations.RenameField(
            model_name='cloud',
            old_name='contact_email_2',
            new_name='Contact email 2',
        ),
        migrations.RenameField(
            model_name='cloud',
            old_name='contact_email_3',
            new_name='Contact email 3',
        ),
        migrations.RenameField(
            model_name='cloud',
            old_name='contact_name_1',
            new_name='Contact name 1',
        ),
        migrations.RenameField(
            model_name='cloud',
            old_name='contact_name_2',
            new_name='Contact name 2',
        ),
        migrations.RenameField(
            model_name='cloud',
            old_name='contact_name_3',
            new_name='Contact name 3',
        ),
        migrations.RenameField(
            model_name='cloud',
            old_name='contact_phone_1',
            new_name='Contact phone 1',
        ),
        migrations.RenameField(
            model_name='cloud',
            old_name='contact_phone_2',
            new_name='Contact phone 2',
        ),
        migrations.RenameField(
            model_name='cloud',
            old_name='contact_phone_3',
            new_name='Contact phone 3',
        ),
        migrations.RenameField(
            model_name='cloud',
            old_name='project_name',
            new_name='Name of project',
        ),
        migrations.RenameField(
            model_name='cloud',
            old_name='project_id',
            new_name='Project ID',
        ),
        migrations.RenameField(
            model_name='cloud',
            old_name='scope',
            new_name='Scope of work',
        ),
        migrations.RenameField(
            model_name='cloud',
            old_name='work_order_valid',
            new_name='Work order valid till',
        ),
    ]
