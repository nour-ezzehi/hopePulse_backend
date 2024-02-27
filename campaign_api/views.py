from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from campaign.models import Campaign, Category, City
from .serializers import CampaignSerializer, CategorySerializer, CitySerializer
from rest_framework import generics
from campaign.models import Campaign
from .serializers import CampaignSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


class CampaignList(generics.ListCreateAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

class CampaignDetail(generics.RetrieveDestroyAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def campaign_list(request):
    if request.method == 'GET':
        campaigns = Campaign.objects.all()
        serializer = CampaignSerializer(campaigns, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Set the owner field to the current authenticated user (request.user)
        request.data['owner'] = request.user.id

        print("Request data:", request.data)  # Print the request data
        serializer = CampaignSerializer(data=request.data)
        if serializer.is_valid():
            print("Serializer is valid.")  # Print a message if the serializer is valid
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("Serializer is not valid. Errors:", serializer.errors)  # Print the errors if the serializer is not valid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def campaign_detail(request, pk):
    try:
        campaign = Campaign.objects.get(pk=pk)
    except Campaign.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CampaignSerializer(campaign)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CampaignSerializer(campaign, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        campaign.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def city_list(request):
    if request.method == 'GET':
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def city_detail(request, pk):
    try:
        city = City.objects.get(pk=pk)
    except City.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CitySerializer(city)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CitySerializer(city, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        city.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)

    print(user.email)
    if user is not None:
        login(request, user)
        refresh = RefreshToken.for_user(user)
        return Response({
            'success': 'Login successful',
            'token': str(refresh.access_token),
            'refresh_token': str(refresh),
            'username': user.username
        })
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    try:
        refresh_token = request.data.get('refresh_token')
        if refresh_token:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'success': 'Logout successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No refresh token provided'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def signup_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(email=email).exists():
        return Response({'error': 'email already exists'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password, email=email)
    user.save()

    return Response({'message': 'User created successfully', "username": user.username, "email": email}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_auth(request):
    """
    Check if the user is authenticated and return user data.
    """
    user = request.user
    user_data = {
        'username': user.username,
        'email': user.email,
    }
    return Response({'authenticated': True, 'user': user_data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_campaigns(request):
    user_campaigns = Campaign.objects.filter(owner=request.user)
    serializer = CampaignSerializer(user_campaigns, many=True)
    return Response(serializer.data)
