import unittest
from app.models import User

class TestUser(unittest.TestCase):
    """
    Test case class to test the properties of the user class
    """
    def setUp(self):
        self.new_user = User(password = 'keton')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)
        
    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('keton'))