# Generated by Django 3.2.6 on 2021-08-30 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('emp_no', models.IntegerField()),
                ('dept', models.CharField(max_length=60)),
                ('age', models.IntegerField()),
                ('mobile', models.IntegerField()),
                ('address', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.IntegerField()),
                ('eemp_no', models.IntegerField()),
            ],
        ),
    ]