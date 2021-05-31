"""User Account Management module."""

from __future__ import absolute_import
try:
    from urllib.parse import urljoin  # python 3
except ImportError:
    from urlparse import urljoin  # python 2
import requests
from furl import furl


class User(object):
    """User class.

    Requests to the user account balance endpoints are equivalent to calling
    the organization account balance endpoints with the personal organization.
    """

    def __init__(self, client):
        """Save a reference to the client."""
        self.client = client

    def get_info(self):
        """Get Current User.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'users/me')
        url = furl(url).add({'apikey': self.client.api_key}).url
        resp = requests.get(url)
        return resp.json()

    def get_balance(self):
        """Get Current Balance.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'users/me/balance')
        url = furl(url).add({'apikey': self.client.api_key}).url
        resp = requests.get(url)
        return resp.json()

    def add_balance(self, amount):
        """Add Balance.

        Charge the user's configured billing source and add that amount
        to your account balance.

        Args:
            amount (float): Amount to add to current user balance.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'users/me/balance')
        url = furl(url).add({'apikey': self.client.api_key}).url
        params = {
            'addamount': amount
        }
        resp = requests.post(url, json=params)
        return resp.json()

    def balance_history(self):
        """Get Balance History.

        Retreive a history of transactions (credits and charges).

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'users/me/balancehistory')
        url = furl(url).add({'apikey': self.client.api_key}).url
        resp = requests.get(url)
        return resp.json()
