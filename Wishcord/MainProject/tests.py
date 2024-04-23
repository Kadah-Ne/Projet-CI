from django.test import TestCase
from MainProject.models import User, Group
import MainProject.dbFunctions as dbf
from MainProject.views import *
from django.shortcuts import render,redirect,reverse


class DbTestCase(TestCase) :
    def setUp(self) -> None:
        self.groupNameWorking = "groupeTest"
        self.groupNameNotWorking = None

        self.usernameWorking = "testerbob"
        self.usernameNotWorking = None

        self.userTest = User.objects.create(username = "testerbob", isAdmin=False)
        self.groupTest = Group.objects.create(name = "groupeTest")

        self.workNbMess = "Should return 1 and work"
        self.errNbMess = "Should return Exception and not work"

        self.workNotNullMess = "Should not be 0"
        self.errNotNullMess = "Should be 0"
    def testCreateGroupWorking(self) :
        self.assertTrue(dbf.createGroup(self.groupNameWorking),self.workNbMess)
        self.assertTrue(dbf.deleteUser(self.groupNameWorking),self.workNbMess)
    
    def testCreateGroupWorking(self) :
        self.assertFalse(dbf.createGroup(self.groupNameNotWorking),self.errNbMess)
        self.assertFalse(dbf.deleteGroup(self.groupNameNotWorking),self.errNbMess)

    def testCreateUser(self) :
        self.assertTrue(dbf.createUser(self.usernameWorking),self.workNbMess)
        self.assertTrue(dbf.deleteUser(self.usernameWorking),self.workNbMess)
    
    def testCreateGroupWorking(self) :
        self.assertFalse(dbf.createUser(self.usernameNotWorking),self.errNbMess)
        self.assertFalse(dbf.deleteUser(self.usernameNotWorking),self.errNbMess)

    def testAddUser2Group(self):
        dbf.createGroup(self.groupNameWorking)
        dbf.createUser(self.usernameWorking)
        self.assertTrue(dbf.addToGroup(self.usernameWorking,self.groupNameWorking))
        self.assertTrue(dbf.removeFromGroup(self.usernameWorking,self.groupNameWorking))
        dbf.deleteGroup(self.groupNameWorking)
        dbf.deleteUser(self.usernameWorking)

    def testGetGroups(self):
        self.assertNotEqual(dbf.getGroups(),0,self.workNotNullMess)
        dbf.createGroup("TestGroup2")
        self.assertNotEqual(dbf.getGroups(),0,self.workNotNullMess)
        dbf.deleteGroup("TestGroup2")

    def testGetUsers(self):
        self.assertNotEqual(dbf.getAllUsers(),0,self.workNotNullMess)
        dbf.createUser("User2")
        self.assertNotEqual(dbf.getAllUsers(),0,self.workNotNullMess)
        dbf.deleteUser("User2")

    def testGetUser(self):
        self.assertEqual(dbf.getUser(self.usernameWorking),self.userTest,self.workNotNullMess)
        self.assertNotEqual(dbf.getUser(self.usernameNotWorking),self.userTest,self.errNotNullMess)
    def testGetGroup(self) :
        self.assertEqual(dbf.getGroup(self.groupNameWorking),self.groupTest,self.workNotNullMess)
        self.assertEqual(dbf.getGroup(self.groupNameNotWorking),None,self.errNotNullMess)
    def testGetUsersFromGroup(self):
        dbf.addToGroup(self.usernameWorking,self.groupNameWorking)
        self.assertEqual(dbf.getUsersFromGroup(self.groupNameWorking),[self.userTest],self.workNotNullMess)
        self.assertNotEqual(dbf.getUsersFromGroup(self.groupNameNotWorking),[self.userTest],self.errNotNullMess)

    def testGetCountUsersFromGroup(self):
        dbf.addToGroup(self.usernameWorking,self.groupNameWorking)
        self.assertEqual(dbf.getCountUsersFromGroup(self.groupNameWorking),1,self.workNotNullMess)
        self.assertNotEqual(dbf.getCountUsersFromGroup(self.groupNameNotWorking),1,self.errNotNullMess)

    def test_groupList_not_authenticated_user(self):
            url = reverse(groupList)
            response = self.client.get(url)
            self.assertTemplateNotUsed(response, 'MainProject/listGroups.html')
            self.failUnlessEqual(response.status_code, 302)
