from django.apps import apps
from django.test import TestCase
from api.apps import YuthanceapiConfig


class YuthanceConfigTest(TestCase):
    """ Test app config name is set correctly
    """

    def test_apps(self):
        self.assertEqual(YuthanceapiConfig.name, 'api')
        self.assertEqual(apps.get_app_config('api').name, 'api')
