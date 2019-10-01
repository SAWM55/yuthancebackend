from django.apps import apps
from django.test import TestCase
from api.apps import YuthanceapiConfig


class YuthanceConfigTest(TestCase):

    def test_apps(self):
        self.assertEqual(YuthanceapiConfig.name, 'api')
        self.assertEqual(apps.get_app_config('api').name, 'api')
