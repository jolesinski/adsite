from django.test import TestCase

# Create your tests here.
from django.utils import timezone
from adverts.models import Advert


class AdvertMethodTests(TestCase):

    def test_has_expired_with_expired_advert(self):
        """
        has_expired() should return True for adverts whose
        expire_date is in the past
        :return:
        """
        time = timezone.now() - datetime.timedelta(days=30)
        expired_ad = Advert(expire_date=time)


class IndexViewTests(TestCase):

    def test_has_expired_with_expired_advert(self):
        """
        has_expired() should return True for adverts whose
        expire_date is in the past
        :return:
        """
        time = timezone.now() - datetime.timedelta(days=30)
        expired_ad = Advert(expire_date=time)