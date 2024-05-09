import io
import pandas

from atlassian import Confluence
from bs4 import BeautifulSoup

from .common import get_confluence


def process(
    url, space, title, delim=",", token=None, username=None, password=None, **kwargs
):
    confluence = get_confluence(
        url=url, token=token, username=username, password=password
    )

    data = get_csv(confluence=confluence, space=space, title=title, **kwargs)

    return data.to_csv(sep=delim)


def get_csv(confluence: Confluence, space, title, **kwargs) -> pandas.DataFrame:
    csv_page = confluence.get_page_by_title(
        space=space, title=title, expand="body.storage"
    )

    if csv_page:
        html = csv_page["body"]["storage"]["value"]
        soup = BeautifulSoup(html, "html.parser")
        table = soup.find("table")

        df = pandas.read_html(io.StringIO(str(table)), **kwargs)[0]

        return df

    return None
