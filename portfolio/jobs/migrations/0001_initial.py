# Generated by Django 2.2.3 on 2019-08-30 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),#20190831 this is the primary key automatically generated by Django for you; though you can create a new field to be another primary key
                ('image', models.ImageField(upload_to='images/')),
                ('summary', models.CharField(max_length=500)),
            ],
        ),
    ]
