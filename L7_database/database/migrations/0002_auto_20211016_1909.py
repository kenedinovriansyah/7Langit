# Generated by Django 3.2.8 on 2021-10-16 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbevent',
            name='banner',
            field=models.ImageField(null=True, upload_to='banner/'),
        ),
        migrations.AlterField(
            model_name='tbcategory',
            name='public_id',
            field=models.CharField(default='wgJG9ajNQcsjzlm4zkcTc', max_length=225, unique=True),
        ),
        migrations.AlterField(
            model_name='tbevent',
            name='public_id',
            field=models.CharField(default='6MvqJ7uUo5Aq_F7NWQi9o', max_length=225, unique=True),
        ),
        migrations.AlterField(
            model_name='tbschedulers',
            name='public_id',
            field=models.CharField(default='-W1UmTetzj17fEL_yaOIF', max_length=225, unique=True),
        ),
    ]
