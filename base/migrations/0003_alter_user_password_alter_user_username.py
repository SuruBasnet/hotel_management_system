# Generated by Django 4.2.2 on 2023-07-13 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_alter_user_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(default="Hari", max_length=200),
        ),
    ]