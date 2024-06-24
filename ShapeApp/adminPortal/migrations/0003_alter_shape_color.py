# Generated by Django 4.2.13 on 2024-06-24 08:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("adminPortal", "0002_alter_shape_color"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shape",
            name="color",
            field=models.CharField(
                choices=[
                    ("Red", "Red"),
                    ("Green", "Green"),
                    ("Blue", "Blue"),
                    ("Yellow", "Yellow"),
                    ("Orange", "Orange"),
                    ("Purple", "Purple"),
                    ("Pink", "Pink"),
                    ("Brown", "Brown"),
                    ("Black", "Black"),
                    ("White", "White"),
                    ("Gray", "Gray"),
                    ("Silver", "Silver"),
                    ("Gold", "Gold"),
                ],
                max_length=255,
            ),
        ),
    ]