from django.test import TestCase
from MainProject.models import User, Group
import MainProject.dbFunctions as dbf


class DbTestCase(TestCase) :
    def setUp(self) -> None:
        User.objects.create(username = "testerbob", isAdmin=False)
        Group.objects.create(name = "groupeTest")
    
    def testAddUser2Groupe(self): 
        user = User.objects.get(username="testerbob")
        groupe = Group.objects.get(name="groupeTest")
    
        self.assertTrue(dbf.addToGroup(user, groupe))

    def testRemoveFromGroup(self):
        user = User.objects.get(username="testerbob")
        groupe = Group.objects.get(name="groupeTest")
    
        self.assertTrue(dbf.removeFromGroup(user, groupe))

    def testCreateGroup(self):
        groupe = Group.objects.get(name="groupeTest")
    
        self.assertTrue(dbf.createGroup(groupe))  

    def testDeleteGroup(self):
        groupe = Group.objects.get(name="groupeTest")
    
        self.assertTrue(dbf.createGroup(groupe))

    def testGetUser(self):
        user = User.objects.get(username="testerbob")

        self.assertTrue(dbf.getUser(user))

    def testGetUsersFromGroup(self):
        groupe = Group.objects.get(name="groupeTest")

        self.assertTrue(dbf.getUsersFromGroup(groupe))

    def testGetAllUsers(self):

        self.assertTrue(dbf.getAllUsers())

    def testCreateUser(self):
        user = User.objects.get(username="testerbob")

        self.assertTrue(dbf.createUser(user))

    def testDeleteUser(self):
        user = User.objects.get(username="testerbob")

        self.assertTrue(dbf.deleteUser(user))