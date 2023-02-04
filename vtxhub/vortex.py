from typing import Optional
import requests

from .models import Interception


class Client:
    BASE = 'https://api.vtxhub.com/v1'
    TIMEOUT = 30

    class VortexError(Exception):
        pass

    def __init__(self):
        self.access_token = None

    def _handle_vortex_errors(self, resp: requests.Response) -> None:
        try:
            data = resp.json()
        except ValueError:
            return

        error = data.get('error', {})
        if error:
            raise self.VortexError(f'{error}')

    def _request(self, method: str, url: str, data: Optional[dict] = None) -> dict:
        headers = {}
        if self.access_token:
            headers['Authorization'] = f'Bearer {self.access_token}'
        response = requests.request(method, url, headers=headers, json=data, timeout=self.TIMEOUT)
        self._handle_vortex_errors(response)
        return response.json()

    def login(self, username: str, password: str) -> None:
        url = f'{self.BASE}/oauth/token'
        auth_data = {
            "grant_type": 'password_grant',
            "username": username,
            "password": password,
        }
        token_data = self._request('post', url, auth_data)
        self.access_token = token_data['data']['access_token']

    def poll(self, app: str) -> list:
        url = f'{self.BASE}/poll'
        filter_data = {
            'interception': {
                'status': 'new',
                'webapp': app,
            },
        }
        data = self._request('post', url, data=filter_data)
        interceptions = data['data'].get('interceptions', [])

        interceptions = [
            Interception(**interception) for interception in interceptions
        ]

        return interceptions
