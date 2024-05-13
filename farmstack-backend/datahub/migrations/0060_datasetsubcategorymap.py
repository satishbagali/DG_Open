# Generated by Django 4.1.5 on 2024-01-08 13:03

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("datahub", "0059_category_subcategory_resourcesubcategorymap"),
    ]

    operations = [
        migrations.CreateModel(
            name="DatasetSubCategoryMap",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "dataset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="dataset_map",
                        to="datahub.datasetv2",
                    ),
                ),
                (
                    "sub_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="dataset_sub_category_map",
                        to="datahub.subcategory",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]