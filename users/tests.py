from django.test import TestCase
from django.test import Client
# Create your tests here.
from django.contrib.auth import get_user_model
from django.urls import reverse,resolve
from django.test import TestCase
from .views import SignupPageView
from .forms import CustomUserCreationForm

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

# class SignUpPageTests(TestCase):
#
#     def setUp(self):
#         url = reverse('signup')
#         self.response = self.client.get(url)
#
#     def test_signup_template(self):
#         self.assertEqual(self.response.status_code, 200)
#         self.assertTemplateUsed(self.response, 'signup.html')
#         self.assertContains(self.response, 'Sign Up')
#         self.assertNotContains(
#             self.response, "hello hi sites"
#         )
#
#     def test_signup_form(self):
#         form = self.response.context.get('form')
#         self.assertIsInstance(form, CustomUserCreationForm)
#         self.assertContains(self.response, 'csrfmiddlewaretoken')
#
#     def test_signup_view(self):
#         view = resolve('/accounts/signup/')
#
#         self.assertEqual(
#             view.func.__name__,
#             SignupPageView.as_view().__name__
#         )

class SignupTests(TestCase):
    username = 'newuser'
    email = 'newuser@gmail.com'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response,'account/signup.html')
        self.assertContains(self.response,'Sign Up')
        self.assertNotContains(self.response, "hiyaa")

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        #
        self.assertEqual(get_user_model().objects.all().count(),1)
        self.assertEqual(get_user_model().objects.all()[0].username,self.username)
        self.assertEqual(get_user_model().objects.all()[0].email,self.email)












