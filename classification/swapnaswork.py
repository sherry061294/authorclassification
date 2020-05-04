import os
authorName = []

for filename in os.listdir(os.getcwd() + '/data/generated_data/2gram'):
    filename_full_path = os.getcwd() + '/data/generated_data/2gram/'+ filename
    if filename.startswith('perp_'):
        continue
    with open(filename_full_path, 'r') as f:
        authorName.append(filename.split('_')[0])
        filedata = f.read()
        filedata_without_start_tag = filedata.replace("<s>","")
        filedata_without_start_end_tag = filedata_without_start_tag.replace(" </s>\n",".")
        # print(filedata_without_start_end_tag)
        