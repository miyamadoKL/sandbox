import yaml

def vault_constructor(loader, node):
    return loader.construct_scalar(node)


def vault_representer(dumper, data):
    if isinstance(data, str) and "ANSIBLE_VAULT" in data:
        return dumper.represent_scalar(u'!vault', data, style='|')

    return dumper.represent_scalar('tag:yaml.org,2002:str', data)


def read_from_file(file_name):
    with open(file_name,"r") as f:
      yaml.add_constructor(u'!vault', vault_constructor)
      return yaml.load(f)


def write_to_file(data):
    with open(file_name,"w") as f:
      yaml.add_representer(str, vault_representer)
      f.write(yaml.dump(data, explicit_start=True, default_flow_style=False))


def nested(dict, list, answer, n=0):
    if n < len(list) - 1:
        dict[list[n]] = {}
        nested(dict[list[n]], list, answer, n + 1)
    else:
        dict[list[n]] = answer


def merge_dict(dict1, dict2, key_list, n=0):
    if len(key_list) <= n:
        print('Can\'t merge dict2 to the same key nested less than dict1.')
        return

    if key_list[n] in dict1 and isinstance(dict1[key_list[n]], dict):
        merge_dict(dict1[key_list[n]], dict2[key_list[n]], key_list, n + 1)
    else:
        dict1.update(dict2)
        

file_name = 'hoge.yml'
data = read_from_file(file_name)

hogedict = {}
key = 'mysql.second_db.another_user'
hogelist = key.split('.')
hogeanswer = 'aiueo'

nested(hogedict, hogelist, hogeanswer)

merge_dict(data['nested_values'], hogedict, hogelist)
# print(data)
write_to_file(data)
