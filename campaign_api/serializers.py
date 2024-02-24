from rest_framework import serializers 
from campaign.models import Campaign, Category, City


class CampaignSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source = 'category.name')
    city_name = serializers.CharField(source = 'city.name', read_only=True)
    class Meta:
        model = Campaign
        fields = ['id', 'name', 'owner', 'start_date', 'telephone_number', 'beneficiary', 'budget', 'category_name', 'city_name', 'story']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
