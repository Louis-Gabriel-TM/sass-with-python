import os
import sys
import sass

FILENAME = "main"

css_file = open( f"{FILENAME}.css", "w", encoding="utf-8")
default_stdout = sys.stdout
sys.stdout = css_file

with open(f"{FILENAME}.scss", "r") as scss_file:
  print(str(sass.compile(string=scss_file.read())))
  sys.stdout = default_stdout
  print(f"{FILENAME}.scss compilated to {FILENAME}.css")