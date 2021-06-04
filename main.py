from genericpath import isdir
import os
import sys



def convert(input_folder, output_folder):
    base_path = os.path.dirname(os.path.dirname(__file__))
    print(base_path)
    input_path = base_path +'/'+ input_folder # os.path.join(base_path, input_folder) # base_path +'/'+ input_folder
    output_path = base_path +'/'+ output_folder # os.path.join(base_path, output_folder) # base_path +'/'+ output_folder

    if os.path.isdir(output_path):
        print("folder exist!")
    else:
        os.makedirs(output_path)
    print(input_path)
    for file in os.listdir(input_path):
        input_file = input_path +'/'+ file # os.path.join(input_path, file) # input_path +'/'+ file
        print(input_file)
        if '.mov' in file.lower():
            output_file = output_path +'/'+ file.lower().replace('.mov','.mp4') # os.path.join(output_path, file.lower().replace('.mov','.mp4')) # output_path +'/'+ file.lower().replace('.mov','.mp4')
            command = f"ffmpeg -i {input_file} {output_file}"
            d = os.popen(command)
            print(d.read())

if __name__ == '__main__':
    convert('test','test123')
    # convert(sys.argv[1], sys.argv[2])