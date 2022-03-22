from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model

from django.test import TestCase


class CustomTests(TestCase):


    def test_create_user(self):

        User = get_user_model()

        user = User.objects.create(
            username='hash',
            email='hash@gmail.com',
            password='hash'
        )

        self.assertEqual(user.username, 'hash')
        self.assertEqual(user.email, 'hash@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()

        user = User.objects.create_superuser(
            username='super',
            email='super@gmail.com',
            password='super'
        )

        self.assertEqual(user.username, 'super')
        self.assertEqual(user.email, 'super@gmail.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


