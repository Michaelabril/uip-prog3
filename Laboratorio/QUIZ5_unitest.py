import unittest

class registro:
    try:
        def registro(self,users,edad):
            users=input("NAME ")
            year=input("YEARS ")
            return {"usuario:":users,"apellido":users+"Michael","edad:":year}
    except Exception:
        print("ERROR")

class NotificationsTestCase(unittest.TestCase):
    try:

        def test_user_repository(self):
            user=registro()
            user=user.registro("Michael","21")
    except Exception:
        print("ERROR")

if __name__ == '__main__':
        unittest.main()