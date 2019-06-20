import yaml

def read_from_file(file_name):
  with open(file_name,"r") as f:
    return yaml.load(f)


def write_to_file(data):
  with open(file_name,"w") as f:
    f.write(yaml.dump(data, explicit_start=True, default_flow_style=False))


def nested(dict, list, answer, n=0):
    if n < len(list) - 1:
        dict[list[n]] = {}
        nested(dict[list[n]], list, answer, n + 1)
    else:
        dict[list[n]] = answer
        

file_name = 'hoge.yml'
data = read_from_file(file_name)

hogedict = {}
key = 'mysql.second_db.another_user'
hogelist = key.split('.')
hogeanswer = 'aiueo'

nested(hogedict, hogelist, hogeanswer)

data['nested_values'][hogelist[0]].update(hogedict[hogelist[0]])

write_to_file(data)
