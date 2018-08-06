import digdag
import datetime

def after5minutes(sessiontime):
  print(sessiontime)
  changing_time = int(sessiontime)
  print(datetime.datetime.fromtimestamp(changing_time))
  print(datetime.datetime.fromtimestamp(changing_time) + datetime.timedelta(minutes=5))
