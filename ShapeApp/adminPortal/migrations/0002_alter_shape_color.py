# Generated by Django 4.2.13 on 2024-06-24 07:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("adminPortal", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shape",
            name="color",
            field=models.CharField(
                choices=[
                    ("Circle", "Circle"),
                    ("Square", "Square"),
                    ("Rectangle", "Rectangle"),
                    ("Triangle", "Triangle"),
                    ("Pentagon", "Pentagon"),
                    ("Hexagon", "Hexagon"),
                    ("Heptagon", "Heptagon"),
                    ("Octagon", "Octagon"),
                    ("Nonagon", "Nonagon"),
                    ("Decagon", "Decagon"),
                    ("Ellipse", "Ellipse"),
                    ("Parallelogram", "Parallelogram"),
                    ("Trapezoid", "Trapezoid"),
                    ("Rhombus", "Rhombus"),
                    ("Star", "Star"),
                    ("Heart", "Heart"),
                    ("Crescent", "Crescent"),
                    ("Arrow", "Arrow"),
                    ("Diamond", "Diamond"),
                    ("Cross", "Cross"),
                    ("Sphere", "Sphere"),
                    ("Cube", "Cube"),
                    ("Cylinder", "Cylinder"),
                    ("Cone", "Cone"),
                    ("Pyramid", "Pyramid"),
                    ("Torus", "Torus"),
                ],
                max_length=255,
            ),
        ),
    ]