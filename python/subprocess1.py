import re
import subprocess
import datetime

def main():
  # Get current time
  curr_time = datetime.datetime.now()

  # Get the name of all files in the current directory with subprocess
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
      file_ts = ps2.stdout.strip()
      print(file_ts)

      # Calculate time delta between current time and file timestamp
      delta = curr_time - datetime.datetime.fromtimestamp(int(file_ts))
      print(delta)
      if delta > datetime.timedelta(minutes=5):
        print("Created older than 5 minutes.")
      else:
        print("Created within 5 minutes.")

if __name__ == "__main__":
  main()
