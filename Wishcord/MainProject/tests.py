from django.test import TestCase
from MainProject.models import User, Group
import MainProject.dbFunctions as dbf


class DbTestCase(TestCase) :
    def setUp(self) -> None:
        self.groupNameWorking = "groupeTest"
        self.groupNameNotWorking = None

        self.usernameWorking = "testerbob"
        self.usernameNotWorking = None

        # self.userTest = User.objects.create(username = "testerbob", isAdmin=False)
        # self.groupTest = Group.objects.create(name = "groupeTest")

        self.workMess = "Should return 1 and work"
        self.errMess = "Should return Exception and not work"

    def testCreateGroupWorking(self) :
        self.assertTrue(dbf.createGroup(self.groupNameWorking),self.workMess)
        self.assertTrue(dbf.deleteUser(self.groupNameWorking),self.workMess)
    
    def testCreateGroupWorking(self) :
        self.assertFalse(dbf.createGroup(self.groupNameNotWorking),self.errMess)
        self.assertFalse(dbf.deleteGroup(self.groupNameNotWorking),self.errMess)

    def testCreateUser(self) :
        self.assertTrue(dbf.createUser(self.usernameWorking),self.workMess)
        self.assertTrue(dbf.deleteUser(self.usernameWorking),self.workMess)
    
    def testCreateGroupWorking(self) :
        self.assertFalse(dbf.createUser(self.usernameNotWorking),self.errMess)
        self.assertFalse(dbf.deleteUser(self.usernameNotWorking),self.errMess)

    def testAddUser2Group(self):
        dbf.createGroup(self.groupNameWorking)
        dbf.createUser(self.usernameWorking)
        self.assertTrue(dbf.addToGroup(self.usernameWorking,self.groupNameWorking))
        self.assertTrue(dbf.removeFromGroup(self.usernameWorking,self.groupNameWorking))
        dbf.deleteGroup(self.groupNameWorking)
        dbf.deleteUser(self.usernameWorking)

    # def testAddUser2Groupe(self): 
    #     self.assertTrue(dbf.addToGroup("testerbob", "groupeTest"))
        

    # def testRemoveFromGroup(self):   
    #     self.assertTrue(dbf.removeFromGroup("testerbob", "groupeTest"))

    # def testCreateGroup(self):
    #     self.assertTrue(dbf.createGroup("groupeTest"))  

    # def testDeleteGroup(self):
    #     groupe = Group.objects.get(name="groupeTest")
    
    #     self.assertTrue(dbf.createGroup(groupe))

    # def testGetUser(self):
    #     user = User.objects.get(username="testerbob")
        
    #     self.assertEqual(dbf.getUser(user),user)

    # def testGetUsersFromGroup(self):
    #     users = User.objects.filter(group = "1")

    #     self.assertEquals(users,dbf.getUsersFromGroup("groupeTest"))

    # def testGetAllUsers(self):
    #     users = User.objects.all()
    #     self.assertEquals(users,dbf.getAllUsers())

    # def testCreateUser(self):
    #     # user = User.objects.get(username="testerbob")

    #     self.assertTrue(dbf.createUser("testerbob"))

    # def testDeleteUser(self):
    #     user = User.objects.get(username="testerbob")

    #     self.assertTrue(dbf.deleteUser(user))