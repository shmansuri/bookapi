# Generated by Django 5.0.4 on 2024-08-05 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('Author', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=100)),
                ('cover_img', models.ImageField(upload_to='')),
                ('rating', models.FloatField()),
            ],
        ),
    ]