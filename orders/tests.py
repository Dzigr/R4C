from django.test import Client, TestCase
from django.urls import reverse

from services import get_json_data


class OrderRobotViewTest(TestCase):
    fixtures = ['fixtures/robots.json']
    test_data = get_json_data('order_data')

    def setUp(self):
        self.client = Client()
        self.add_order_url = reverse('order_robot')

    def test_order_robot_view_valid_data(self):
        json_data = self.test_data.get('valid_order_data')
        response = self.client.post(
            self.add_order_url,
            json_data,
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {'message': 'Robot with serial AB-11 is available for purchase'},
        )

    def test_order_robot_view_invalid_data(self):
        json_data = self.test_data.get('invalid_order_data')
        response = self.client.post(
            self.add_order_url,
            json_data,
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn(
            'Enter a valid email address.',
            response.json()['error']['email'],
        )
