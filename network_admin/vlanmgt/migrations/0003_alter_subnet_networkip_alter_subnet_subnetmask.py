# Generated by Django 4.0 on 2022-01-04 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vlanmgt', '0002_alter_vlan_vlanname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subnet',
            name='Networkip',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='subnet',
            name='SubnetMask',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
