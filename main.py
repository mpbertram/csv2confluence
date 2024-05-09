import io
import json
import argparse
import pandas

from csv2confluence import confluence

def expand_json(data):
    return pandas.read_json(
        io.StringIO(pandas.json_normalize(json.loads(data)).to_json())
    )

def main():
  parser = argparse.ArgumentParser(
    prog='confluence',
    description='exports csv data to confluence'
  )
  
  parser.add_argument('-i', '--input', required=True, help='Input directory where to find CSV files')
  parser.add_argument('-d', '--delimiter', default=',', help='CSV delimiter')
  
  parser.add_argument('-a', '--aggBy', default=None, help='Aggregate CSV data by given column')
  parser.add_argument('-xj', '--expandJson', default=None, help='Column name to expand JSON')
  
  parser.add_argument('-w', '--url', default='https://confluence.rz.bankenit.de/confluence', help='Confluence URL')
  parser.add_argument('-t', '--token', help='Confluence token, preferred over username/password')
  parser.add_argument('-u', '--username', help='Confluence username, not used if token is set')
  parser.add_argument('-p', '--password', help='Confluence password, not used if token is set')
  parser.add_argument('-s', '--space', required=True, help='Confluence space')
  parser.add_argument('-e', '--parent', required=True, help='Confluence parent page ID')
  
  args = parser.parse_args()
  
  confluence.process(
    input=args.input,
    url=args.url,
    space=args.space,
    parent=args.parent,
    csv_delim=args.delimiter,
    agg_by=args.aggBy,
    expand_fns={args.expandJson: expand_json} if args.expandJson else None,
    token=args.token,
    username=args.username,
    password=args.password,
    parent_page_fn=None,
    sub_page_fmt_fn=None
  )

if __name__ == "__main__":
  main()
