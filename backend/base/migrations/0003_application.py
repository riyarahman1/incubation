# Generated by Django 4.1.3 on 2022-11-09 06:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_alluserdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50, null=True)),
                ('phone', models.IntegerField(null=True)),
                ('company_name', models.CharField(max_length=500, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=500, null=True)),
                ('image', models.ImageField(null=True, upload_to='images')),
                ('companyurl', models.CharField(max_length=50, null=True)),
                ('TypeOfincubation', models.CharField(max_length=500, null=True)),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('DECLINED', 'DECLINED'), ('APPROVED', 'APPROVED')], default='PENDING', max_length=100, null=True)),
                ('approved', models.BooleanField(default=False)),
                ('declined', models.BooleanField(default=False)),
                ('pending', models.BooleanField(default=True)),
                ('allotted', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
