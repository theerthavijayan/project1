# Generated by Django 3.2.8 on 2022-05-13 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AjaxCrud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(max_length=100)),
                ('Password', models.TextField()),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Phone', models.BigIntegerField(unique=True)),
            ],
        ),
    ]