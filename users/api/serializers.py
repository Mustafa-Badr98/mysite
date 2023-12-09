from django.forms import ValidationError
from rest_framework import serializers
from users.models import NewUser
from rest_framework import validators
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
# from favorites.api.serializers import FavoriteSerializer

# UserModel = get_user_model()


class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = '__all__'


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = '__all__'

    def create(self, clean_data):
        user_obj = NewUser.objects.create_user(
            email=clean_data['email'], password=clean_data['password'], user_name=clean_data['user_name'])
        user_obj.mobile_phone = clean_data['mobile_phone']
        user_obj.location = clean_data['location']
        user_obj.save()
        return user_obj


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def check_user(self, clean_data):
        user = authenticate(
            username=clean_data['email'], password=clean_data['password'])
        if not user:
            return 0

        return user


class UserSerializer(serializers.ModelSerializer):
   
  
    class Meta:
        model = NewUser
        fields = '__all__'


    # id = serializers.IntegerField(read_only=True)
    # email = serializers.EmailField(max_length=100)
    # user_name = serializers.CharField(max_length=200,required=False)
    # first_name=serializers.CharField(required=False)
    # last_name = serializers.CharField(required=False)
    # mobile_phone=serializers.IntegerField(required=False)
    # profile_pic= serializers.ImageField(required=False)
    # created_at = serializers.DateTimeField(read_only=True)
    # updated_at = serializers.DateTimeField(read_only=True)

    # def create(self, validated_data):
    #     return  NewUser.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.title = validated_data['title']
    #     instance.description = validated_data['description']
    #     instance.area_size=validated_data['area_size']
    #     instance.price = validated_data['price']
    #     instance.location = validated_data['location']
    #     instance.number_of_bedrooms = validated_data['number_of_bedrooms']
    #     instance.number_of_bathrooms = validated_data['number_of_bathrooms']
    #     instance.image = validated_data['image']
    #     instance.lat = validated_data['lat']
    #     instance.lon = validated_data['lon']
    #     instance.save()
    #     return  instance


class AddAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = '__all__'

    def create(self, clean_data):
        user_obj = NewUser.objects.create_user(
            email=clean_data['email'], password=clean_data['password'], user_name=clean_data['user_name'])
        user_obj.mobile_phone = clean_data['mobile_phone']
        user_obj.location = clean_data['location']
        user_obj.is_admin = True
        user_obj.save()
        return user_obj
