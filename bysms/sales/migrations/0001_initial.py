# Generated by Django 2.1.4 on 2020-07-04 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('user_phone', models.CharField(max_length=200)),
                ('user_addr', models.CharField(max_length=200)),
            ],
        ),
    ]
