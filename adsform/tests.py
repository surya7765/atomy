from django.test import TestCase

from django.test import TestCase
from django.urls import reverse

class HomeViewTest(TestCase):
    def test_home_view_status_code(self):
        """
        Test that the home view returns a 200 OK status code.
        """
        # The `reverse` function gets the URL for a named URL pattern from urls.py file.
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_view_uses_correct_template(self):
        """
        Test that the home view uses the 'index.html' template.
        """
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'index.html')

    def test_home_view_has_form_in_context(self):
        """
        Test that the home view context contains a MessageForm instance.
        """
        url = reverse('home')
        response = self.client.get(url)
        self.assertIn('form', response.context)
        self.assertEqual(response.context['form'].__class__.__name__, 'MessageForm')