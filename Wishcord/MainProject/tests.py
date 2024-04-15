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
        
        self.assertEqual(dbf.getUser(user),user)

    def testGetUsersFromGroup(self):
        users = User.objects.filter(group = "1")

        self.assertQuerySetEqual(users,dbf.getUsersFromGroup("groupeTest"))

    def testGetAllUsers(self):
        users = User.objects.all()
        print(users)
        self.assertQuerySetEqual(users,dbf.getAllUsers())

    def testCreateUser(self):
        user = User.objects.get(username="testerbob")

        self.assertTrue(dbf.createUser(user))

    def testDeleteUser(self):
        user = User.objects.get(username="testerbob")

        self.assertTrue(dbf.deleteUser(user))