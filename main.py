import argparse 
import custom_functions

parser = argparse.ArgumentParser("simple_parser")
parser.add_argument("file_directory", help="file path to be read", type=str)
parser.add_argument("new_file_name", help="new file name", type=str)
args = parser.parse_args()

print('reading file: ' + args.file_directory)

file = open(args.file_directory, 'r')

path = custom_functions.remove_file_from_path(args.file_directory, args.new_file_name)
new_file = open(path, 'w')    

lines = file.readlines()

aux = 0
for val in lines: 
    if len(val) == 6:
        new_file.write(val)
        aux+=1
new_file.close()

custom_functions.count_lines(path)
print('Zenilton C Cardoso')
file.close()
