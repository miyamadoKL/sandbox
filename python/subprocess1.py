import re
import subprocess
import datetime

def main():
  sp1 = subprocess.run(["ls"], stdout=subprocess.PIPE, universal_newlines=True)
  files = sp1.stdout
  print(files)
  #=>xxx.py
  #=>yyy.ipynb
  #=>zzz.py
  #=>...

  print(files.split())
  #=>['xxx.py', 'yyy.ipynb', 'zzz.py', ...]

  for file in files.split():
    if re.search(".ipynb", file):
      print(file)
      cmd = "gls -l --time-style='+%s' " + file + " | tr -s ' ' | cut -d' ' -f 6"
      ps2 = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
      print(ps2.stdout.strip())

if __name__ == "__main__":
  main()
