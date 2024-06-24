from django.db import models

# Create your models here.
class Shape(models.Model):
    SHAPE_CHOICES = (
        ('Circle', 'Circle'),
        ('Square', 'Square'),
        ('Rectangle', 'Rectangle'),
        ('Triangle', 'Triangle'),
        ('Pentagon', 'Pentagon'),
        ('Hexagon', 'Hexagon'),
        ('Heptagon', 'Heptagon'),
        ('Octagon', 'Octagon'),
        ('Nonagon', 'Nonagon'),
        ('Decagon', 'Decagon'),
        ('Ellipse', 'Ellipse'),
        ('Parallelogram', 'Parallelogram'),
        ('Trapezoid', 'Trapezoid'),
        ('Rhombus', 'Rhombus'),
        ('Star', 'Star'),
        ('Heart', 'Heart'),
        ('Crescent', 'Crescent'),
        ('Arrow', 'Arrow'),
        ('Diamond', 'Diamond'),
        ('Cross', 'Cross'),
        ('Sphere', 'Sphere'),
        ('Cube', 'Cube'),
        ('Cylinder', 'Cylinder'),
        ('Cone', 'Cone'),
        ('Pyramid', 'Pyramid'),
        ('Torus', 'Torus'),
    )

    COLOR_CHOICES = (
        ('Red', 'Red'),
        ('Green', 'Green'),
        ('Blue', 'Blue'),
        ('Yellow', 'Yellow'),
        ('Orange', 'Orange'),
        ('Purple', 'Purple'),
        ('Pink', 'Pink'),
        ('Brown', 'Brown'),
        ('Black', 'Black'),
        ('White', 'White'),
        ('Gray', 'Gray'),
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
    )

    name = models.CharField(max_length=100)
    shape = models.CharField(max_length=255, choices=SHAPE_CHOICES, blank=False, null=False)
    color = models.CharField(max_length=255, choices=COLOR_CHOICES, blank=False, null=False)
    shape_image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name