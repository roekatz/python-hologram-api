"""Data Plans module."""

from __future__ import absolute_import
try:
    from urllib.parse import urljoin  # python 3
except ImportError:
    from urlparse import urljoin  # python 2
import requests
from furl import furl


class DataPlans(object):
    """DataPlans class.

    The Data Plans endpoints return pricing and descriptions for the different
    data plans that Hologram offers. When changing the data plan for a cellular
    link via API, you must refer to the plan by its ID, which you can determine
    from these endpoints.
    """

    def __init__(self, client):
        """Save a reference to the client."""
        self.client = client

    def list(self):
        """List Data Plans.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'plans')
        url = furl(url).add({'apikey': self.client.api_key}).url
        resp = requests.get(url)
        return resp.json()

    def get(self, plan_id):
        """Get a Data Plan.

        Args:
            plan_id (int): The ID of the plan to get.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'plans/{}'.format(plan_id))
        url = furl(url).add({'apikey': self.client.api_key}).url
        resp = requests.get(url)
        return resp.json()
