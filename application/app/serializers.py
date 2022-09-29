from rest_framework import serializers
from.models import Art


class Artserializers(serializers.ModelSerializer):
    class Meta:
        model=Art
        fields=['id','title','auther','emil','date']
