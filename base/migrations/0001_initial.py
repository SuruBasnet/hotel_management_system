# Generated by Django 4.2.2 on 2023-06-30 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bill",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("amount", models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="CustomerProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("customer_name", models.CharField(max_length=300)),
                ("customer_age", models.IntegerField()),
                ("customer_address", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="GuestProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("guest_name", models.CharField(max_length=100)),
                ("guest_age", models.IntegerField()),
                ("guest_address", models.CharField(max_length=300)),
                ("guest_number", models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Menu",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("food_name", models.CharField(max_length=100)),
                (
                    "fodd_type",
                    models.CharField(
                        choices=[
                            ("Vegeterian", "Vegeterian"),
                            ("Non-vegeterian", "Non-vegeterian"),
                        ],
                        max_length=100,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RoomInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("room_no", models.IntegerField()),
                ("room_bed_count", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="RoomService",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("service_name", models.CharField(max_length=200)),
                ("service_description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="RoomType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("type_name", models.CharField(max_length=100)),
                ("type_info", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="RoomInfoService",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "room_info",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="base.roominfo",
                    ),
                ),
                (
                    "service",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="base.roomservice",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="roominfo",
            name="room_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="base.roomtype",
            ),
        ),
        migrations.CreateModel(
            name="GuestOrganization",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("organization_name", models.CharField(max_length=300)),
                ("organization_address", models.TextField()),
                ("organization_ceo_name", models.CharField(max_length=200)),
                (
                    "guest_profile",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="base.guestprofile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CustomerPayment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("payment_amount", models.BigIntegerField()),
                (
                    "payment_type",
                    models.CharField(
                        choices=[
                            ("Esewa", "Esewa"),
                            ("Khalit", "Khalti"),
                            ("Online banking", "Online banking"),
                            ("Offline", "Offline"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "bill",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="base.bill",
                    ),
                ),
                (
                    "customer_profile",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="base.customerprofile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                (
                    "customer_profile",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="base.customerprofile",
                    ),
                ),
                (
                    "room",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="base.roominfo",
                    ),
                ),
            ],
        ),
    ]