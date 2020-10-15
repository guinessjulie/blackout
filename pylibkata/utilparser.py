
import re
def removeChars(org_str, removing_chars) :
    return ''.join(c for c in org_str if c not in removing_chars)

# allow only lowercase letters,numbers,underscore
def validate_usr(username):
    return re.match(r'^[a-z0-9_]{4,16}$', username) != None

def begin_with2(n, chars) :
    return str(n)[0] in chars

def begin_with(n, chars):
    return str(n).startswith(chars)

# count lowercase letter
import re
# my solution
def lowercase_count2(strng):    
    return len(re.sub(r'[^a-z]', '', strng))

# best solution using islower()
def lowercase_count3(strng):
    return sum(x.islower() for x in strng)

# re.findall()
def lowercase_count4(strng):
    return len(re.findall(r'[a-z]', strng))

# lambda
lowercase_count = lambda strng : sum(c.islower() for c in strng)

# 7kyu
# remove Vowels from all sentences
def disemvowel2(string):
    cns = ''
    for c in string :
        if c not in 'aeiouAEIOU':
            cns += c
    return cns

# join and for if
def disemvowel(string):
    return ''.join(c for c in string if c.lower() not in 'aeiou')

#pin only accept 4 or 6 digit
def validate_pin2(pin):
    if '\n' in pin : 
        return False # trick
    return re.match(r'^[0-9]{4}$|^[0-9]{6}$', pin) != None

# proper solution

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

#mysolution
def vowel_start(st): 
    st = re.sub(r'[\s|\W|^_]', '', st.lower())
    print(st)
    encode = ''
    for x in st :
        if(x in 'aeiou') : 
            encode+=' '+x
        else :
            encode += x
    return encode.strip()

#kata answer .. I don't understand it
from re import sub
def vowel_start(st):
    return sub(r'(?<=.)([aeiou])', r' \1', sub(r'[^a-z0-9]', '', st.lower()))
            

print(vowel_start('It is beautiful weather today!'))
print('it isb e a ut if ulw e ath ert od ay')
print(vowel_start('Coding is great'))
print('c od ing isgr e at')
print(vowel_start('my number is 0208-533-2325'))
print('myn umb er iss02085332325' )
print(vowel_start('oranges, apples, melon, pineapple'))
print('or ang es appl esm el onp in e appl e' )
print(vowel_start('under_score'))
print('und ersc or e')