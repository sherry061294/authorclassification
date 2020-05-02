import os


count = 0
for filename in os.listdir(os.getcwd() + '/Unusable/'):
    filename_full_path = os.getcwd() + '/Unusable/'+ filename
    f = open(filename_full_path, 'r')
    # x = f.read()
    count +=1
    print(filename)
    for txt_line in f:
        print(count)
        print(filename)
        print(txt_line)   

    
