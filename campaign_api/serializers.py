from rest_framework import serializers
from campaign.models import Campaign, Category, City, Charity, Donation, Comment

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

class CharitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Charity
        fields = ['id', 'name', 'owner', 'telephone_number', 'email', 'address']

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ['id', 'donor_user', 'amount', 'transaction_date', 'recipient_type', 'recipient_id']

    # Override the to_representation method to include the recipient_object in the serialized data
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # Add recipient_object field to the serialized data
        recipient_object = instance.recipient_object
        if recipient_object:
            if isinstance(recipient_object, Campaign):
                representation['recipient_object'] = CampaignSerializer(recipient_object).data
            elif isinstance(recipient_object, Charity):
                representation['recipient_object'] = CharitySerializer(recipient_object).data
        
        return representation

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = ['id', 'owner,', 'text', 'published_date']
