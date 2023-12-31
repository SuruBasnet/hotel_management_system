# Generated by Django 4.2.2 on 2023-07-14 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0007_alter_guestprofile_created_at_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="usertype",
            field=models.CharField(
                choices=[
                    ("Frontdesk", "Frontdesk"),
                    ("Admin", "Admin"),
                    ("Accounting", "Accounting"),
                    ("Restaurant", "Restaurant"),
                ],
                default="Admin",
                max_length=50,
            ),
            preserve_default=False,
        ),
    ]
