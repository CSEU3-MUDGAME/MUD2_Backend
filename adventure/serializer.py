from rest_framework import serializers

class RoomSerializer(serializers.Serializer):
    items = serializers.CharField(max_length=500, default="")
    n_to = serializers.IntegerField(default=0)
    s_to = serializers.IntegerField(default=0)
    e_to = serializers.IntegerField(default=0)
    w_to = serializers.IntegerField(default=0)
    up = serializers.BooleanField(default=False)
    down = serializers.BooleanField(default=False)
    left = serializers.BooleanField(default=False)
    right = serializers.BooleanField(default=False)