from django.test import TestCase

# Create your tests here.

from django.test import Client, TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth.models import Permission

from .models import Book, Review


class BookTest(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title="New Book",
            author="New Author",
            price="55.55"
        )



        self.user = get_user_model().objects.create_user(username="newuser",
                                                    password="newpassword",
                                                    email="newuser@gmail.com")

        self.special_permission = Permission.objects.get(codename='special_status')

        self.review = Review.objects.create(review="new review",
                                            book=self.book,
                                            author=self.user,
                                            )

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', "New Book")
        self.assertEqual(self.book.author,"New Author")
        self.assertEqual(self.book.price, '55.55')

    def test_book_list_view_for_logged_in_user(self):
        self.client.login(username='newuser', email='newuser@gmail.com', password='newpassword')
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response, 'New Book')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_list_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '%s?next=/books/' % (reverse('account_login')))

        response = self.client.get('%s?next=/books/' % (reverse('account_login')))
        self.assertContains(response, 'Log In')

    def test_book_Detail_view_with_permissions(self):
        self.client.login(email='newuser@gmail.com',username='newuser', password='newpassword')
        self.user.user_permissions.add(self.special_permission)
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'New Book')
        self.assertContains(response, 'new review')
        self.assertTemplateUsed(response, 'books/book_detail.html')
    # def test_book_list_view(self):
    #     response = self.client.get(reverse('book_list'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "New Book")
    #     self.assertTemplateUsed(response, 'books/book_list.html')
    #
    #
    # def test_book_detail_view(self):
    #     response = self.client.get(self.book.get_absolute_url())
    #     no_response = self.client.get('/books/1234/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(no_response.status_code,404)
    #     self.assertContains(response,'New Book')
    #     self.assertContains(response, "new review")
    #     self.assertTemplateUsed(response, 'books/book_detail.html')

