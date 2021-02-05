from difflib import get_close_matches
import json
data = json.load(open('./data.json'))

# function to find defination
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys())) >0:
        yn=input(f'Did you mean {get_close_matches(word,data.keys())[0]}? Y-yes,N-no\n')
        if yn == 'Y' or yn =='y':
            return translate(get_close_matches(word,data.keys())[0])
        else:
            return 'We doesn\'t understand your entry.'			
    else:
        print('Word does\'nt exist.Please check the word you have entered')	



word = input('Enter a word: ')
output = translate(word)

if type(output)==list:
    for defination in output:
        print(defination)
else:
    print(output)        
