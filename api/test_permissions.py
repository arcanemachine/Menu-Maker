from django.contrib.auth.models import AnonymousUser
from django.urls import reverse
from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework import permissions

import factories as f
from restaurants.models import Restaurant
from menus.models import Menu, MenuSection, MenuItem
from api.permissions import HasRestaurantPermissionsOrReadOnly

class HasRestaurantPermissionsOrReadOnlyTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.factory = APIRequestFactory()
        cls.test_permission = HasRestaurantPermissionsOrReadOnly()

        # create users
        cls.admin_user = f.UserFactory(username='admin_user', is_staff=True)
        cls.permitted_user = f.UserFactory(username='permitted_user')
        cls.non_permitted_user = f.UserFactory(username='non_permitted_user')


    def setUp(self):
        # create restaurant objects and add permitted user to admin_users
        self.test_restaurant = f.RestaurantFactory(
            admin_users=[self.permitted_user])
        self.test_menu = f.MenuFactory(restaurant=self.test_restaurant)
        self.test_menusection = f.MenuSectionFactory(menu=self.test_menu)
        self.test_menuitem = \
            f.MenuItemFactory(menusection=self.test_menusection)

    def test_unauthenticated_user_returns_false(self):
        request = self.factory.get('/')
        request.user = AnonymousUser()

        obj = None

        self.assertFalse(
            self.test_permission.has_object_permission(request, None, obj))

    def test_admin_user_returns_true(self):
        request = self.factory.delete('/')
        request.user = self.admin_user

        obj = None

        self.assertTrue(
            self.test_permission.has_object_permission(request, None, obj))

    def test_non_permitted_user_can_use_safe_methods(self):
        request = self.factory.get('/')
        request.user = self.non_permitted_user

        obj = None

        self.assertTrue(request.method in permissions.SAFE_METHODS)
        self.assertTrue(
            self.test_permission.has_object_permission(request, None, obj))

    def test_permitted_user_with_restaurant_object(self):
        request = self.factory.delete('/')
        request.user = self.permitted_user

        obj = self.test_restaurant

        self.assertTrue(
            self.test_permission.has_object_permission(request, None, obj))

    def test_permitted_user_with_menu_object(self):
        request = self.factory.delete('/')
        request.user = self.permitted_user

        obj = self.test_menu

        self.assertTrue(
            self.test_permission.has_object_permission(request, None, obj))

    def test_permitted_user_with_menusection_object(self):
        request = self.factory.delete('/')
        request.user = self.permitted_user

        obj = self.test_menusection

        self.assertTrue(
            self.test_permission.has_object_permission(request, None, obj))

    def test_permitted_user_with_menuitem_object(self):
        request = self.factory.delete('/')
        request.user = self.permitted_user

        obj = self.test_menuitem

        self.assertTrue(
            self.test_permission.has_object_permission(request, None, obj))

    def test_permitted_user_with_non_restaurant_object(self):
        request = self.factory.delete('/')
        request.user = self.permitted_user

        obj = AnonymousUser

        with self.assertRaises(TypeError):
            self.test_permission.has_object_permission(request, None, obj)

    # edge cases
    def test_non_permitted_user_with_restaurant_object(self):
        request = self.factory.delete('/')
        request.user = self.non_permitted_user

        obj = self.test_restaurant

        self.assertFalse(
            self.test_permission.has_object_permission(request, None, obj))
