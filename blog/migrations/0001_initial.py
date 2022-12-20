# Generated by Django 4.1.3 on 2022-12-02 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=50)),
                ("node0", models.CharField(max_length=1)),
                ("node1", models.CharField(max_length=1)),
                ("node2", models.CharField(max_length=1)),
                ("node3", models.CharField(max_length=1)),
                ("node4", models.CharField(max_length=1)),
                ("node5", models.CharField(max_length=1)),
                ("node6", models.CharField(max_length=1)),
                ("node7", models.CharField(max_length=1)),
                ("node8", models.CharField(max_length=1)),
            ],
        ),
    ]
