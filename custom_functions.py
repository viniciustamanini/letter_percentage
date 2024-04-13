from Letter import Letter

def remove_file_from_path(file_path, new_file_name):
    x = file_path.split('/')
    x.pop()
    path = '/'.join(x)
    path=path+'/'+new_file_name

    return path

def word_has_five_letters(word):
    return len(word) == 5

def count_lines(path):
    file = open(path, 'r')
    lines = file.readlines()
    total_lines = len(lines) + 1
    total_letters = sum(len(word.rstrip()) for word in lines)
    print('lines ', str(total_lines), ' letters ', str(total_letters))
    count_letters(lines, total_letters)
    file.close()
    
    return total_letters

def count_letters(line, total_letters):   
    _letter_list = []

    for word in line:
        for letter in word.lower().rstrip():    
            l = Letter(letter)

            letter_from_list = next(
                    (obj for obj in _letter_list if obj.letter == letter), 
                    None
                    )
            if bool(letter_from_list):
                letter_from_list.__iterate__()
            else:
                _letter_list.append(l)    
    
    _letter_list.sort(reverse=True, key=(lambda x: x.iterator))
    calculate_and_print_percentage(_letter_list, total_letters)

def calculate_and_print_percentage(letter_list, total_letters):
    for letter in letter_list:
       print(letter.letter, ' | '
             , letter.iterator, ' | '
             , round(((letter.iterator/total_letters) * 100), 2),'%' )
