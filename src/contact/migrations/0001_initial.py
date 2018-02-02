# Generated by Django 2.0.2 on 2018-02-02 03:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240)),
                ('address', models.CharField(blank=True, max_length=240, null=True)),
                ('phone_number', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(max_length=240)),
                ('realtor', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=10)),
                ('contact_pref', models.CharField(choices=[('email', 'Email'), ('phone', 'Phone')], default='email', max_length=10)),
                ('contact_time_pref', models.CharField(choices=[('morning', 'Morning'), ('afternoon', 'Afternoon'), ('evening', 'Evening')], default='evening', max_length=20)),
                ('message', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
