import os

try:
    cr = bs.decode('utf8')
except UnicodeDecodeError:
    cr = bs.decode('latin1')
for filename in os.listdir(os.getcwd() + '/final/data/processed_data/'):
    filename_full_path = os.getcwd() + '/final/data/processed_data/'+ filename
    print(filename)
    with open(filename_full_path, 'r') as f:
        filedata = f.read()