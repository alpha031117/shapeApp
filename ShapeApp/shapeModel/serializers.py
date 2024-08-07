from rest_framework import serializers
from .models import Shape
from django.contrib.auth.models import User
from django.utils import timezone

class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension
    
class ShapeSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    shape_image = Base64ImageField(max_length=None, use_url=True, required=False)

    class Meta:
        model = Shape
        fields = '__all__'
        read_only_fields = ['name', 'created_at']

    def create(self, validated_data):
        validated_data['name'] = self.context['request'].user.username
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.created_at = timezone.now()

        # Update only fields that are present in validated_data
        instance.shape = validated_data.get('shape', instance.shape)
        instance.color = validated_data.get('color', instance.color)
        # Handling optional field shape_image
        if 'shape_image' in validated_data:
            instance.shape_image = validated_data['shape_image']

        instance.save()
        return instance
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
