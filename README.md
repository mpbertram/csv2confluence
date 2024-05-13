# `csv2confluence`
From CSV to Confluence and the other way around.

## CSV to Confluence
```
usage: confluence [-h] -i INPUT [-d DELIMITER] [-a AGGBY] [-xj EXPANDJSON] [-w URL] [-t TOKEN] [-u USERNAME] [-p PASSWORD] -s SPACE -e PARENT

exports csv data to confluence

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input directory where to find CSV files
  -d DELIMITER, --delimiter DELIMITER
                        CSV delimiter
  -a AGGBY, --aggBy AGGBY
                        Aggregate CSV data by given column
  -xj EXPANDJSON, --expandJson EXPANDJSON
                        Column name to expand JSON
  -w URL, --url URL     Confluence URL
  -t TOKEN, --token TOKEN
                        Confluence token, preferred over username/password
  -u USERNAME, --username USERNAME
                        Confluence username, not used if token is set
  -p PASSWORD, --password PASSWORD
                        Confluence password, not used if token is set
  -s SPACE, --space SPACE
                        Confluence space
  -e PARENT, --parent PARENT
                        Confluence parent page ID
```

## Confluence to CSV
```
usage: csv [-h] [-d DELIMITER] [-w URL] [-t TOKEN] [-u USERNAME] [-p PASSWORD] -s SPACE -e TITLE

transforms confluence table into CSV

optional arguments:
  -h, --help            show this help message and exit
  -d DELIMITER, --delimiter DELIMITER
                        CSV delimiter
  -w URL, --url URL     Confluence URL
  -t TOKEN, --token TOKEN
                        Confluence token, preferred over username/password
  -u USERNAME, --username USERNAME
                        Confluence username, not used if token is set
  -p PASSWORD, --password PASSWORD
                        Confluence password, not used if token is set
  -s SPACE, --space SPACE
                        Confluence space
  -e TITLE, --title TITLE
                        Title of page with table
```
