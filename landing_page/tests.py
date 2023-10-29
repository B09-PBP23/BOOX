from django.test import TestCase
from django.urls import reverse
from django.test import Client
from .forms import *
from .models import *

# Create your tests here.
class FormTest(TestCase):
    def test_form_valid_data(self):
        form = FAQForm(data={
            "category": "other", 
            "question": "This is a test question that should be accepted",
            "is_public": True
        })

        self.assertTrue(form.is_valid())

        form = FAQForm(data={
            "category": "other", 
            "question": "This is a test question that should be accepted too",
            "is_public": False
        })
        self.assertTrue(form.is_valid())

        form = FAQForm(data={
            "category": "other", 
            "question": "This is a test question that should be accepted eitherway",
            "is_public": True
        })

        self.assertTrue(form.is_valid())

class ViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        response = self.client.get(reverse('landing_page:show_landing_page'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "BooX - Awesome Book Website")
        self.assertContains(response, "Browse Now")
        self.assertContains(response, "Search By:")
        self.assertContains(response, "Search:")
        self.assertContains(response, "Discover More")

    def test_is_user_logged_in(self):
        response = self.client.get(reverse('landing_page:check_if_user_logged_in'))
        self.assertIn(response.content.decode(), ['true', 'false'])
    
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('landing_page:show_landing_page'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_render(self):
        response = self.client.get(reverse('landing_page:show_landing_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'landing_page.html')

class BookModelTest(TestCase):
    def setUp(self):
        Books.objects.create(title="Book 1", author="Author 1", publisher="Publisher 1", total_ratings=0, total_reviews=0)
        Books.objects.create(title="Book 2", author="Author 2", publisher="Publisher 2", total_ratings=0, total_reviews=0)
        Books.objects.create(title="Book 3", author="Author 3", publisher="Publisher 3", total_ratings=0, total_reviews=0)

    def test_book_model(self):
        book1 = Books.objects.get(title="Book 1")
        book2 = Books.objects.get(title="Book 2")
        book3 = Books.objects.get(title="Book 3")

        self.assertEqual(book1.author, "Author 1")
        self.assertEqual(book2.author, "Author 2")
        self.assertEqual(book3.author, "Author 3")

        self.assertEqual(book1.publisher, "Publisher 1")
        self.assertEqual(book2.publisher, "Publisher 2")
        self.assertEqual(book3.publisher, "Publisher 3")
    
    def test_book_model_total_ratings(self):
        book1 = Books.objects.get(title="Book 1")
        book2 = Books.objects.get(title="Book 2")
        book3 = Books.objects.get(title="Book 3")

        self.assertEqual(book1.total_ratings, 0)
        self.assertEqual(book2.total_ratings, 0)
        self.assertEqual(book3.total_ratings, 0)

    def test_book_model_total_reviews(self):
        book1 = Books.objects.get(title="Book 1")
        book2 = Books.objects.get(title="Book 2")
        book3 = Books.objects.get(title="Book 3")

        self.assertEqual(book1.total_reviews, 0)
        self.assertEqual(book2.total_reviews, 0)
        self.assertEqual(book3.total_reviews, 0)
    
    def test_book_model_image_url(self):
        book1 = Books.objects.get(title="Book 1")
        book2 = Books.objects.get(title="Book 2")
        book3 = Books.objects.get(title="Book 3")

        self.assertEqual(book1.image_url_s, None)
        self.assertEqual(book2.image_url_s, None)
        self.assertEqual(book3.image_url_s, None)

        self.assertEqual(book1.image_url_m, None)
        self.assertEqual(book2.image_url_m, None)
        self.assertEqual(book3.image_url_m, None)

        self.assertEqual(book1.image_url_l, None)
        self.assertEqual(book2.image_url_l, None)
        self.assertEqual(book3.image_url_l, None)
    
    def test_book_model_year(self):
        book1 = Books.objects.get(title="Book 1")
        book2 = Books.objects.get(title="Book 2")
        book3 = Books.objects.get(title="Book 3")

        self.assertEqual(book1.year, None)
        self.assertEqual(book2.year, None)
        self.assertEqual(book3.year, None)

class FAQModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(username="testuser")
        FAQ.objects.create(user=user, category="other", question="Question 1", answer="Answer 1", is_public=True)
        FAQ.objects.create(user=user, category="other", question="Question 2", answer="Answer 2", is_public=False)
        FAQ.objects.create(user=user, category="other", question="Question 3", answer="Answer 3", is_public=True)
    
    def test_faq_model(self):
        faq1 = FAQ.objects.get(question="Question 1")
        faq2 = FAQ.objects.get(question="Question 2")
        faq3 = FAQ.objects.get(question="Question 3")

        self.assertEqual(faq1.category, "other")
        self.assertEqual(faq2.category, "other")
        self.assertEqual(faq3.category, "other")

        self.assertEqual(faq1.answer, "Answer 1")
        self.assertEqual(faq2.answer, "Answer 2")
        self.assertEqual(faq3.answer, "Answer 3")

        self.assertEqual(faq1.is_public, True)
        self.assertEqual(faq2.is_public, False)
        self.assertEqual(faq3.is_public, True)