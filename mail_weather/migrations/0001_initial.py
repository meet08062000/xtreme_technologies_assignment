# Generated by Django 4.0 on 2022-01-04 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('city', models.CharField(choices=[('Mum', 'Mumbai'), ('Del', 'Delhi'), (
                    'Che', 'Chennai'), ('Ban', 'Bangalore'), ('Kol', 'Kolkata')], max_length=20)),
                ('time', models.TimeField()),
            ],
        ),
    ]
