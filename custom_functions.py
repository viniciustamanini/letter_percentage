from Letter import Letter

def remove_file_from_path(file_path, new_file_name):
    x = file_path.split('/')
    x.pop()
    path = '/'.join(x)
    path=path+'/'+new_file_name

    return path

def count_lines(path):
    file = open(path, 'r')
    lines = file.readlines()
    total_lines = len(lines)
    total_letters = total_lines * 5
    print('lines ', str(total_lines), ' letters ', str(total_letters))
    count_letters(lines, total_letters)
    file.close()
    
    return total_letters

def count_letters(line, total_letters):   
    _letter_list = [Letter()]

    for word in line:
        for letter in word.lower().strip():    
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
    i = 0
    for letter in _letter_list:
       print(_letter_list[i].letter, ' | '
             , _letter_list[i].iterator, ' | '
             , round(((_letter_list[i].iterator/total_letters) * 100), 2),'%' )
       i+=1

