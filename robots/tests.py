import os

from django.test import Client, TestCase
from django.urls import reverse

from services import get_json_data

from .services import ExcelGenerator


class CreateRobotViewTestCase(TestCase):
    test_data = get_json_data('robot_data')

    def setUp(self):
        self.client = Client()
        self.add_robot_url = reverse('add_robot')

    def test_create_robot_successfully(self):
        json_data = self.test_data.get('valid_robot_data')
        response = self.client.post(
            self.add_robot_url,
            json_data,
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {"message": "Robot with serial AB-01 created successfully"},
        )

    def test_create_robot_invalid_date(self):
        json_data = self.test_data.get('invalid_date')
        response = self.client.post(
            self.add_robot_url,
            json_data,
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(),
            {"error": {"created": ["Enter a valid date/time."]}},
        )

    def test_create_robot_invalid_model(self):
        json_data = self.test_data.get('invalid_model')
        response = self.client.post(
            self.add_robot_url,
            json_data,
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(),
            {"error": {"model": [
                "Ensure this value has at most 2 characters (it has 3)."
            ]}},
        )


class ExcelGeneratorTestCase(TestCase):
    fixtures = ['fixtures/robots.json']

    def setUp(self):
        self.client = Client()
        self.get_excel_url = reverse('get_excel_data')

    def test_generate_excel_file_exists(self):
        excel_generator = ExcelGenerator()
        file_path = excel_generator.generate_excel()
        self.assertTrue(os.path.exists(file_path))

    def test_generate_excel_file_contains_data(self):
        excel_generator = ExcelGenerator()
        file_path = excel_generator.generate_excel()
        self.assertGreater(os.path.getsize(file_path), 0)

    def test_download_excel_view(self):
        response = self.client.get(self.get_excel_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response['Content-Type'],
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        self.assertIn('attachment; filename="robots_', response['Content-Disposition'])

