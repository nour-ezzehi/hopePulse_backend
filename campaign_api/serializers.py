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
    category = serializers.CharField(source='category.name', required=False)
    city = serializers.CharField(source='city.name', required=False)

    class Meta:
        model = Campaign
        fields = ['id', 'name', 'owner', 'telephone_number', 'beneficiary', 'budget', 'category', 'city', 'story']

    def create(self, validated_data):
        category_name = validated_data.pop('category', None)
        city_name = validated_data.pop('city', None)

        category_id = validated_data.pop('category_id', None)
        city_id = validated_data.pop('city_id', None)

        if category_name:
            category, _ = Category.objects.get_or_create(name=category_name)
            validated_data['category'] = category
        elif category_id:
            validated_data['category_id'] = category_id

        if city_name:
            city, _ = City.objects.get_or_create(name=city_name)
            validated_data['city'] = city
        elif city_id:
            validated_data['city_id'] = city_id

        return Campaign.objects.create(**validated_data)
