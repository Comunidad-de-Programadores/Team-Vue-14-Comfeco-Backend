from django.urls import reverse
from rest_framework.test import force_authenticate, APIClient, APITestCase
from rest_framework import status
from .serializers import UserProfileSerializer, UserChangePasswordSerializer
from .models import User


class UserAPITest(APITestCase):

    def setUp(self):
        self.user1 = User.objects.create(
            username='daniel', email='danielhuamani15@gmail.com', first_name='daniel')
        self.user1.set_password('daniel987')
        self.user2 = User.objects.create(
            username='jorgeperez', email='jorge@gmail.com', first_name='jorge', last_name='perez')
        self.user2.set_password('jorge123')
    
    def test_get_user_profile(self):
        client = APIClient()
        client.force_authenticate(user=self.user1)
        response = client.get(reverse('users:user_profile'))
        serializer = UserProfileSerializer(self.user1)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_user_profile(self):
        client = APIClient()
        client.force_authenticate(user=self.user1)
        data = {
            'username': 'daniel', 'email':'luis@gmail.com', 'first_name':'daniel', 
            'last_name':'perez', 'birth_day': '11/10/2020', 'gender': 'Masculino',
            'country': 'Perú', 'facebook': 'daniel', 'github': 'daniel', 'linkedin': 'daniel',
            'twitter': 'daniel', 'biography': 'desarrollador fullstack'
        }
        response = client.put(reverse('users:user_profile'), data)
        serializer = UserProfileSerializer(self.user1)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_put_user_profile_invalid_fields(self):
        client = APIClient()
        client.force_authenticate(user=self.user1)
        data = {
            'username': 'jorgeperez', 'email':'jorge@gmail.com', 'first_name':'daniel', 
            'last_name':'perez', 'birth_day': '11/10/2020', 'gender': 'Masculino',
            'country': 'Perú', 'facebook': 'daniel', 'github': 'daniel', 'linkedin': 'daniel',
            'twitter': 'daniel', 'biography': ''
        }
        response = client.put(reverse('users:user_profile'), data)
        serializer = UserProfileSerializer(self.user1)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_put_user_change_password(self):
        client = APIClient()
        client.force_authenticate(user=self.user1)
        data = {'old_password': 'daniel987', 'password': 'daniel123', 'password2': 'daniel123'}
        response = client.put(reverse('users:user_change_password'), data)
        serializer = UserChangePasswordSerializer(self.user1)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.user1.check_password('daniel123'))
        self.assertFalse(self.user1.check_password('daniel987'))