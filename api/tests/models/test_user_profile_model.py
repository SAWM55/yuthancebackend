# """This module contains tests for the user profile model

# Author GitHub: @Dave-mash
# """

# from django.test import TestCase
# from ...v1.models.user_model import UserProfile
# from ...models import User


# class TestUserModel(TestCase):

#     def setUp(self):
#         User.objects.create(email='doe@example.com')

#     def test_user_found(self):

#         # user = UserProfile.objects.get(phone_number='254729710290')
#         # self.assertEqual(user.__repr__(), {
#         #     "phone_number": '254729710290',
#         #     "address": 'Eastleigh, Nairobi',
#         #     "city": 'Nairobi'
#         # })
#         user = User.objects.get(email='doe@example.com')
#         self.assertEqual(user.get_user_by_email(), 'doe@example.com')

#         UserProfile.objects.create(
#             user_id=1,
#             phone_number='254729710290',
#             address='Eastleigh, Nairobi',
#             city='Nairobi'
#         )
