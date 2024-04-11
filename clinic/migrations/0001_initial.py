# Generated by Django 5.0.4 on 2024-04-11 20:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('slug', models.SlugField(allow_unicode=True, max_length=200, unique=True, verbose_name='slug')),
                ('content', models.TextField(verbose_name='content')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('bio', models.TextField(verbose_name='bio')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='doctor_photos/', verbose_name='photo')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, max_length=100, null=True, unique=True, verbose_name='slug')),
            ],
        ),
        migrations.CreateModel(
            name='LatestNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('slug', models.SlugField(allow_unicode=True, max_length=200, unique=True, verbose_name='slug')),
                ('content', models.TextField(verbose_name='content')),
            ],
        ),
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, max_length=100, null=True, unique=True, verbose_name='slug')),
                ('address', models.TextField(verbose_name='address')),
                ('phone_number', models.CharField(max_length=15, verbose_name='phone number')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('website', models.URLField(blank=True, null=True, verbose_name='website')),
                ('opening_hours', models.CharField(help_text='e.g. Mon-Fri: 9am-5pm', max_length=100, verbose_name='opening hours')),
                ('description', models.TextField(verbose_name='description')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='clinic_photos/', verbose_name='photo')),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='clinic', to='clinic.doctor', verbose_name='doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clinic', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='clinic.clinic', verbose_name='clinic')),
            ],
        ),
        migrations.CreateModel(
            name='PatientReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100, verbose_name='patient name')),
                ('review', models.TextField(verbose_name='review')),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_reviews', to='clinic.clinic', verbose_name='clinic')),
            ],
        ),
    ]