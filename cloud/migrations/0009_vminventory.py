# Generated by Django 4.0.3 on 2022-12-18 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0008_storage'),
    ]

    operations = [
        migrations.CreateModel(
            name='VmInventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VM_ID', models.IntegerField()),
                ('Department_name', models.CharField(max_length=30)),
                ('Application_name', models.CharField(max_length=30)),
                ('Application_URL', models.URLField()),
                ('App_or_DB_VM', models.CharField(choices=[('APP', 'APP'), ('DB', 'DB')], max_length=10)),
                ('Tenant_IP', models.GenericIPAddressField()),
                ('Provider_IP', models.GenericIPAddressField()),
                ('vCPU', models.IntegerField()),
                ('RAM', models.IntegerField()),
                ('Storage', models.FloatField()),
                ('Physical_server_ID', models.CharField(max_length=30)),
                ('Remarks', models.CharField(max_length=100)),
                ('VM_creation_date', models.DateField()),
            ],
        ),
    ]
