"""Cellular Links module."""

from __future__ import absolute_import
try:
    from urllib.parse import urljoin  # python 3
except ImportError:
    from urlparse import urljoin  # python 2
import requests
from furl import furl


class CellularLinks(object):
    """CellularLinks class.

    A Cellular Link is the association between a Device and a cellular data
    plan and SIM. Typically, a device has exactly one Cellular Link.
    """

    def __init__(self, client):
        """Save a reference to the client."""
        self.client = client

    def activate_sims(self, sims, plan, tier):
        """Activate SIMs.

        Args:
            sims (List[str]): array of SIM numbers to activate.
            plan (int): Device data plan. Look up plan IDs with List Data Plans.
            tier (int): Geographic zone. Currently the valid tiers are 1 and 2.
                    Higher tiers incur higher costs. See pricing for details.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'links/cellular/bulkclaim')
        url = furl(url).add({'apikey': self.client.api_key}).url
        params = {
            'sims': sims,
            'plan': plan,
            'tier': tier
        }
        resp = requests.post(url, json=params)
        return resp.json()

    def list_links(self, org_id=None):
        """List Cellular Links.

        Args:
            org_id (int, optional): Only return results for the given organization ID.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'links/cellular')
        url = furl(url).add({'apikey': self.client.api_key}).url
        params = {
            'orgid': org_id
        }
        resp = requests.get(url, json=params)
        return resp.json()

    def get_link(self, link_id):
        """Get Cellular Link.

        Args:
            link_id (int): Integer ID of the link to retrieve.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'links/cellular/{}'.format(link_id))
        url = furl(url).add({'apikey': self.client.api_key}).url

        resp = requests.get(url)
        return resp.json()

    def change_plan(self, link_id, plan, tier):
        """Change Plan.

        Args:
            link_id (int): Integer ID of the link to change.
            plan (int): Device data plan. Look up plan IDs with List Data Plans.
            tier (int): Geographic zone. Currently the valid tiers are 1 and 2.
                Higher tiers incur higher costs. See pricing for details.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'links/cellular/{}/changeplan'.format(link_id))
        url = furl(url).add({'apikey': self.client.api_key}).url
        params = {
            'plan': plan,
            'tier': tier
        }
        resp = requests.post(url, json=params)
        return resp.json()

    def change_overage_limit(self, link_id, limit):
        """Change Overage Limit.

        Args:
            link_id (int): Integer ID of the link to modify.
            limit (int): Number of bytes over the plan limit to allow. Set -1 for no data limit.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'links/cellular/{}/overagelimit'.format(link_id))
        url = furl(url).add({'apikey': self.client.api_key}).url
        params = {
            'limit': limit
        }
        resp = requests.post(url, json=params)
        return resp.json()

    def pause_link(self, link_id):
        """Pause Data.

        Args:
            link_id (int): Integer ID of the link to modify.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'links/cellular/{}/state'.format(link_id))
        url = furl(url).add({'apikey': self.client.api_key}).url
        params = {
            'state': 'pause'
        }
        resp = requests.post(url, json=params)
        return resp.json()

    def unpause_link(self, link_id):
        """Unpause Data.

        Args:
            link_id (int): Integer ID of the link to modify.

        Returns:
            dict: the json response as a dictionary.
        """
        url = urljoin(self.client.base_url, 'links/cellular/{}/state'.format(link_id))
        url = furl(url).add({'apikey': self.client.api_key}).url
        params = {
            'state': 'live'
        }
        resp = requests.post(url, json=params)
        return resp.json()
