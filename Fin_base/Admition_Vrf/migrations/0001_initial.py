# Generated by Django 4.0.4 on 2022-06-04 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aadher',
            fields=[
                ('aadher_number', models.UUIDField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('fathername', models.CharField(max_length=150)),
                ('mothername', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=250)),
                ('phone', models.BigIntegerField()),
                ('pincode', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='aadher_bio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biodata1', models.CharField(editable=False, max_length=500)),
                ('biodata2', models.CharField(editable=False, max_length=500)),
                ('biodata3', models.CharField(editable=False, max_length=500)),
                ('biodata4', models.CharField(editable=False, max_length=500)),
                ('biodata5', models.CharField(editable=False, max_length=500)),
                ('aadher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admition_Vrf.aadher')),
            ],
        ),
    ]
