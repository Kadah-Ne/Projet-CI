from django.test import TestCase
from MainProject.models import User, Group
import MainProject.dbFunctions as dbf


class DbTestCase(TestCase) :
    def setUp(self) -> None:
        User.objects.create(username = "testerbob", isAdmin=False)
        Group.objects.create( name = "groupeTest")
    
    def testAddUser2Groupe(self): 
        user = User.objects.get(username="testerbob")
        groupe = Group.objects.get(name="groupeTest")
    
        self.assertTrue(dbf.addToGroup(user, groupe))

    