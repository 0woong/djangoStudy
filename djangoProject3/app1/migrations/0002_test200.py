# Generated by Django 3.2.11 on 2022-01-06 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test200',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('content', models.CharField(max_length=300)),
                ('tel', models.CharField(max_length=300)),
            ],
        ),
    ]
