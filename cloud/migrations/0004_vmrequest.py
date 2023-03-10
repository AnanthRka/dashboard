# Generated by Django 4.0.3 on 2022-12-18 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0003_rename_client name_cloud_client_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VmRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_id', models.IntegerField()),
                ('department_id', models.IntegerField()),
                ('department_name', models.CharField(max_length=30)),
                ('request_recieved_detail', models.CharField(max_length=100)),
                ('request_recieved_time', models.TimeField()),
                ('request_from', models.CharField(choices=[('Elcot Official', 'ELCOT Official'), ('Department', 'Department'), ('Developer', 'Developer'), ('DCO', 'DCO')], max_length=30)),
                ('name_official', models.CharField(max_length=30)),
                ('mail_id', models.EmailField(max_length=254)),
                ('phone_num', models.IntegerField()),
                ('organization', models.CharField(max_length=30)),
                ('request_through', models.CharField(choices=[('Mail', 'Mail'), ('Whatsapp', 'Whatsapp'), ('Hard copy', 'Hard copy')], max_length=20)),
                ('request_proof', models.ImageField(upload_to='')),
                ('auth_by', models.CharField(max_length=20)),
                ('auth_proof', models.CharField(max_length=20)),
                ('num_of_vm', models.IntegerField()),
                ('ram', models.IntegerField()),
                ('vcpu', models.IntegerField()),
                ('storage', models.IntegerField()),
                ('os', models.CharField(max_length=30)),
                ('dept_person_name', models.CharField(max_length=30)),
                ('dept_desig', models.CharField(max_length=20)),
                ('dept_mail_id', models.EmailField(max_length=254)),
                ('dept_phone', models.IntegerField()),
                ('dev_person_name', models.CharField(max_length=30)),
                ('dev_desig', models.CharField(max_length=20)),
                ('dev_mail_id', models.EmailField(max_length=254)),
                ('dev_phone', models.IntegerField()),
                ('dev_org', models.CharField(max_length=30)),
                ('approval_cdac', models.CharField(choices=[('Approved', 'Approved'), ('Rejected', 'Rejected')], max_length=20)),
                ('remarks_support_eng', models.CharField(max_length=100)),
                ('remarks_cdac_off', models.CharField(max_length=100)),
            ],
        ),
    ]
