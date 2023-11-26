from rest_framework import serializers


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class CodeVerificationSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=5)


class SessionSerializer(serializers.Serializer):
    fav_color = serializers.CharField()
