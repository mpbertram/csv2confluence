import argparse

from csv2confluence import csv

def main():
  parser = argparse.ArgumentParser(
    prog='csv',
    description='transforms confluence table into CSV'
  )
  
  parser.add_argument('-d', '--delimiter', default=',', help='CSV delimiter')
  
  parser.add_argument('-w', '--url', default='https://confluence.rz.bankenit.de/confluence', help='Confluence URL')
  parser.add_argument('-t', '--token', help='Confluence token, preferred over username/password')
  parser.add_argument('-u', '--username', help='Confluence username, not used if token is set')
  parser.add_argument('-p', '--password', help='Confluence password, not used if token is set')
  parser.add_argument('-s', '--space', required=True, help='Confluence space')
  parser.add_argument('-e', '--title', required=True, help='Title of page with table')
  
  args = parser.parse_args()
  
  data = csv.process(
    url=args.url,
    space=args.space,
    title=args.title,
    delim=args.delimiter,
    token=args.token,
    username=args.username,
    password=args.password,
    thousands='',
    decimal=','
  )
  
  print(data)

if __name__ == "__main__":
  main()
