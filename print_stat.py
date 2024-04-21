import os
import fnmatch
import yaml

cont = 0

for path,dirs,files in os.walk('.'):
    for file in files:
        if fnmatch.fnmatch(file,'results.yaml'):
            fullname = os.path.join(path,file)
            print(fullname)
            with open(fullname, 'r') as stream:
                data_loaded = yaml.safe_load(stream)

            cont += data_loaded[0]['app_0']['iteration']
            #print(data_loaded[0]['app_0']['iteration'])

media = cont/30
print(media)