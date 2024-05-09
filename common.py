import requests

from atlassian import Confluence


def get_confluence(url=None, token=None, username=None, password=None):
    if token:
        session = requests.Session()
        session.headers.update({"Authorization": f"Bearer {token}"})

        return Confluence(url=url, session=session)
    else:
        return Confluence(url=url, username=username, password=password)
