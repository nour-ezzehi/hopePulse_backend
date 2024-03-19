from django.urls import path
from .views import campaign_list, campaign_detail, category_list, category_detail, city_list, city_detail, CampaignDetail, CampaignList, login_view, signup_view, logout_view, check_auth, user_campaigns
from accounts.views import custom_user_detail, custom_user_list

app_name = 'campaign'

urlpatterns = [
    path('<int:pk>/', CampaignDetail.as_view(), name='detailcreate'),
    path('', CampaignList.as_view(), name='listcreate'),
    path('campaigns/', campaign_list, name='campaign-list'),
    path('campaigns/<int:pk>/', campaign_detail, name='campaign-detail'),
    path('categories/', category_list, name='category-list-create'),
    path('categories/<int:pk>/', category_detail, name='category-retrieve-update-destroy'),
    path('cities/', city_list, name='city-list'),
    path('cities/<int:pk>/', city_detail, name='city-detail'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('check-auth/', check_auth),
    path('user-campaigns/', user_campaigns),
    path('users/', custom_user_list, name='user-list'),
    path('users/<int:pk>/', custom_user_detail, name='user-detail')
]
