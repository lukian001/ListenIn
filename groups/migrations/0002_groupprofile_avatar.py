# Generated by Django 4.0.4 on 2022-05-28 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupprofile',
            name='avatar',
            field=models.ImageField(blank=True, default='avatar-default.png', upload_to=''),
        ),
    ]
