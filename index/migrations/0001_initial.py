# Generated by Django 4.1 on 2022-10-02 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
                ('country', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=50)),
                ('passport_number', models.CharField(max_length=50)),
                ('home_address', models.CharField(max_length=150)),
                ('current_address', models.CharField(max_length=150)),
                ('tel_number_home', models.CharField(max_length=50)),
                ('tel_number_mobile', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('name_of_institution', models.CharField(max_length=50)),
                ('address_of_institution', models.CharField(max_length=150)),
                ('degree', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=150)),
                ('major', models.CharField(max_length=150)),
                ('tem_number_of_institution', models.CharField(max_length=50)),
                ('email_of_institution', models.EmailField(max_length=100)),
                ('english', models.CharField(max_length=50)),
                ('korean', models.CharField(max_length=50)),
                ('statement_of_interest', models.TextField()),
            ],
        ),
    ]
