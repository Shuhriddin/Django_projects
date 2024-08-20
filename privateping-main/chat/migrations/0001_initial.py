# Generated by Django 5.0.1 on 2024-02-23 14:35

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("name", models.CharField(max_length=25)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("username", models.CharField(max_length=20, unique=True)),
                ("online", models.IntegerField(default=0)),
                (
                    "online_for",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="chat.userprofile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Messages",
            fields=[
                (
                    "id",
                    models.AutoField(
                        editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("description", models.TextField()),
                ("time", models.TimeField(auto_now_add=True)),
                ("seen", models.BooleanField(default=False)),
                (
                    "timestamp",
                    models.DateTimeField(
                        db_index=True, default=django.utils.timezone.now
                    ),
                ),
                (
                    "receiver_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="receiver",
                        to="chat.userprofile",
                    ),
                ),
                (
                    "sender_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sender",
                        to="chat.userprofile",
                    ),
                ),
            ],
            options={
                "ordering": ("timestamp",),
            },
        ),
        migrations.CreateModel(
            name="Keys",
            fields=[
                (
                    "id",
                    models.AutoField(
                        editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("public_key", models.TextField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="chat.userprofile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Friends",
            fields=[
                (
                    "id",
                    models.AutoField(
                        editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("friend", models.IntegerField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="chat.userprofile",
                    ),
                ),
            ],
        ),
    ]
