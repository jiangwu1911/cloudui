from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import RequestFactory
from django.utils import unittest

from django import http
from django.test.utils import override_settings

from openstack_dashboard import api
from openstack_dashboard.tests import helpers as test


class ServerWrapperTests(test.TestCase):

    def test_get_base_attribute(self):
        server = api.nova.Server(self.servers.first(), self.request)
        self.assertEqual(server.id, self.servers.first().id)

    def test_image_name(self):
        image = self.images.first()
        self.mox.StubOutWithMock(api.glance, 'image_get')
        api.glance.image_get(IsA(http.HttpRequest),
                             image.id).AndReturn(image)
        self.mox.ReplayAll()

        server = api.nova.Server(self.servers.first(), self.request)
        self.assertEqual(server.image_name, image.name)
