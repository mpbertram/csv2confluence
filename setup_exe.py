from cx_Freeze import setup, Executable

executables = [
  Executable("to_confluence.py", base=None),
  Executable("to_csv.py", base=None)
]

packages = [
  'idna',
  'pandas',
  'atlassian',
  'xlsxwriter',
  'bs4',
  'lxml'
]

options = {
  'build_exe': {
    'packages': packages
  }
}

setup(
  name = "csv2confluence",
  options = options,
  version = "0.1",
  description = 'csv to confluence',
  executables = executables
)
