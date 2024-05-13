from pandas import DataFrame
from datetime import datetime
from atlassian import Confluence

from .process import get_data
from .common import get_confluence


def process(
    input,
    url,
    space,
    parent,
    csv_delim=",",
    agg_by=None,
    expand_fns=None,
    token=None,
    username=None,
    password=None,
    parent_page_fn=None,
    sub_page_fmt_fn=None,
):
    confluence = get_confluence(url, token, username, password)

    data = get_data(
        input_dir=input, delim=csv_delim, agg_by=agg_by, expand_fns=expand_fns
    )

    parent = create_parent_page(
        confluence=confluence,
        space=space,
        parent=parent,
        body=create_parent_body(data, parent_page_fn),
    )

    create_sub_pages(confluence, parent, data, sub_page_fmt_fn)

    return parent


def create_sub_pages(confluence: Confluence, parent, data, body_fmt_fn=None):
    for name, payload in data.items():
        confluence.update_or_create(
            parent_id=parent["id"],
            title=f"{name} - {parent['title']}",
            body=get_body(name, payload, body_fmt_fn),
        )


def get_body(name, payload: DataFrame, body_fmt_fn=None):
    if body_fmt_fn is None:
        data = "<p>No data</p>"
        if not payload.empty:
            data = payload.to_html(index=False, decimal=",", na_rep="", max_rows=10000)

        return f"""
        <h1>Data for {name}</h1>
        {data}
      """
    else:
        return body_fmt_fn(name, payload)


def create_parent_page(confluence: Confluence, body, space=None, parent=None):
    return confluence.create_page(
        space=space, parent_id=parent, title=str(datetime.now()), body=body
    )


def create_parent_body(data=None, fmt_fn=None):
    html_body = """
    <h1>Content</h1> 
    <p>
      <ac:macro ac:name="children">
      </ac:macro>
    </p>
  """

    if fmt_fn and data:
        html_body += fmt_fn(data)

    return html_body
