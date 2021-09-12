from django.test import TestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView


# Create your tests here.
class HomepageTest(TestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Homepage')

    def test_homepage_not_contains_correct_html(self):
        self.assertNotContains(self.response, 'Esto no está en lap ágina')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )


class AboutPageTest(TestCase):
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'nosotros.html')

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, 'Nosotros page')

    def test_aboutpage_does_not_contains_incorrect_html(self):
        self.assertNotContains(self.response, 'Puras hueás')

    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve('/nosotros/')
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__,
        )
