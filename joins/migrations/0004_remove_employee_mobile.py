# Generated by Django 3.2.6 on 2021-08-30 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0003_rename_name_employee_emp_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='mobile',
        ),
    ]