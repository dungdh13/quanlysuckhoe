# Generated by Django 3.0.4 on 2020-03-22 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_ho_ten'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='MSBN',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='cd_benh',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='profile',
            name='sdt',
            field=models.BigIntegerField(null=True),
        ),
    ]
