# Generated by Django 3.2.9 on 2021-12-29 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handiApp', '0007_alter_account_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profilePic',
            field=models.ImageField(default='media/handiApp/blankProfilePic.png', upload_to='uploads/'),
        ),
    ]
