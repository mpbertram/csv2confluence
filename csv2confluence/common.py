import requests

from atlassian import Confluence


def get_confluence(
    url: str = None, token: str = None, username: str = None, password: str = None
):
    if token:
        session = requests.Session()
        if url.find('atlassian.net') > -1:
          # Confluence cloud supports Basic Auth
          session.headers.update({"Authorization": f"Basic {token}"})
        else:
          # Confluence OnPrem supports a bearer token
          session.headers.update({"Authorization": f"Bearer {token}"})

        return Confluence(url=url, session=session)
    else:
        return Confluence(url=url, username=username, password=password)
