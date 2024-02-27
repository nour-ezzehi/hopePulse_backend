from rest_framework import serializers
from campaign.models import Campaign, Category, City

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']

class CampaignSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())
    city = serializers.SlugRelatedField(slug_field='name', queryset=City.objects.all())

    class Meta:
        model = Campaign
        fields = ['id', 'name', 'owner', 'telephone_number', 'beneficiary', 'budget', 'category', 'city', 'story']
