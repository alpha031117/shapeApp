# forms.py
from django import forms
from .models import Shape   

class ShapeForm(forms.ModelForm):
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

    shape = forms.ChoiceField(choices=SHAPE_CHOICES, label='Shape Type')
    color = forms.ChoiceField(choices=COLOR_CHOICES, label='Shape Color')
    shape_image = forms.ImageField(label='Shape Image')

    class Meta:
        model = Shape
        fields = ['shape', 'color', 'shape_image']
