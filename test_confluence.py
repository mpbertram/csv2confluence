from csv2confluence import common, confluence, csv
from .to_confluence import expand_json


def test_confluence(url, token, space, parent):
    page = confluence.process(
        input="test-data",
        url=url,
        space=space,
        parent=parent,
        csv_delim=",",
        agg_by="COLUMN1",
        expand_fns={"COLUMN3": expand_json},
        token=token,
    )
    print(page)

    result = csv.process(
        url=url, space=space, title=f"1 - {page['title']}", token=token
    )
    print(result)

    c = common.get_confluence(url, token)
    c.remove_page(page["id"], recursive=True)
