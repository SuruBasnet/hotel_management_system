# Generated by Django 4.2.2 on 2023-07-13 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0005_alter_guestprofile_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="guestprofile",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="guestprofile",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
