
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
def vowel_start2(st): 
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
            
# check exam
# +4 for correct answer, -1 for incorrect, 0 for empty
def check_exam2(arr1,arr2):
    score = 0
    for i, corr in enumerate(arr1) :
        if arr2[i] == "":
            score = score
        elif corr == arr2[i] : 
            score += 4
        elif corr != arr2[i]:
            score -= 1
    return max(score, 0)

# clever way
def check_exam(key,answer ):
    return max(0, sum(4 if a==b else -1 for a, b in zip(key,answer) if b))

# print(check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]), 6)
# print(check_exam(["a", "a", "c", "b"], ["a", "a", "b",  ""]), 7)
# print(check_exam(["a", "a", "b", "c"], ["a", "a", "b", "c"]), 16)
# print(check_exam(["b", "c", "b", "a"], ["",  "a", "a", "c"]), 0)

def get_drink_by_profession2(param):
    orders = ["Jabroni","School Counselor", "Programmer",  "Bike Gang Member",  "Politician"	,  "Rapper"	]
    deliver = ["Patron Tequila",	"Anything with Alcohol", "Hipster Craft Beer", "Moonshine" ,"Your tax dollars","Cristal"]
    for i, order in enumerate(orders) :
        if param.lower() == order.lower() :
            return deliver[i]
    else :
        return 'Beer'

# other solution with tuple?
def get_drink_by_profession(param):
    d = {
    "jabroni": "Patron Tequila",
    "school counselor": "Anything with Alcohol",
    "programmer": "Hipster Craft Beer",
    "bike gang member": "Moonshine",
    "politician": "Your tax dollars",
    "rapper": "Cristal"
    }
    return d.get(param.lower(), 'Beer')

    
# print(get_drink_by_profession("jabrOni"), "Patron Tequila", "'Jabroni' should map to 'Patron Tequila'")
# print(get_drink_by_profession("scHOOl counselor"), "Anything with Alcohol", "'School Counselor' should map to 'Anything with alcohol'")
# print(get_drink_by_profession("prOgramMer"), "Hipster Craft Beer", "'Programmer' should map to 'Hipster Craft Beer'")
# print(get_drink_by_profession("bike ganG member"), "Moonshine", "'Bike Gang Member' should map to 'Moonshine'")
# print(get_drink_by_profession("poLiTiCian"), "Your tax dollars", "'Politician' should map to 'Your tax dollars'")
# print(get_drink_by_profession("rapper"), "Cristal", "'Rapper' should map to 'Cristal'")
# print(get_drink_by_profession("pundit"), "Beer", "'Pundit' should map to 'Beer'")
# print(get_drink_by_profession("Pug"), "Beer", "'Pug' should map to 'Beer'")

#how many alchol should you buy to cover the cost of holiday
import math
def duty_free(price, discount, holiday_cost):
    return  math.floor(holiday_cost / (price * discount/100))

# print(duty_free(12, 50, 1000), 166)
# print(duty_free(17, 10, 500), 294)

welcome_db = {
'english': 'Welcome',
'czech': 'Vitejte',
'danish': 'Velkomst',
'dutch': 'Welkom',
'estonian': 'Tere tulemast',
'finnish': 'Tervetuloa',
'flemish': 'Welgekomen',
'french': 'Bienvenue',
'german': 'Willkommen',
'irish': 'Failte',
'italian': 'Benvenuto',
'latvian': 'Gaidits',
'lithuanian': 'Laukiamas',
'polish': 'Witamy',
'spanish': 'Bienvenido',
'swedish': 'Valkommen',
'welsh': 'Croeso'
}

def greet2(lan):
    try:
        return (welcome_db[lan])
    except:
        return 'Welcome'

# gosu solution
def greet(lan):
    return welcome_db.get(lan, 'Welcome')

#  is it a digit? just one digit is accepted
 
#print("Basic tests")
#print(greet('english'), 'Welcome')
#print(greet('dutch'), 'Welkom')
#print(greet('IP_ADDRESS_INVALID'), 'Welcome')
#print(greet(''), 'Welcome')
#print(greet(2), 'Welcome')

#Regix
import re
def is_digit1(n):
    return re.match(r'\d\Z', n) != None

def is_digit2(n):
    return re.match(r'\d', n) != None and len(n) == 1

#re.fullmatch() 라는 기능도 있었음
def is_digit3(n):
    return re.fullmatch(r'\d',n) != None
#lamda 
is_digit = lambda n : len(n) == 1 and n in '0123456789'

#print(is_digit(""), False)
#print(is_digit("7"), True)
#print(is_digit(" "), False)
#print(is_digit("a"), False)
#print(is_digit("a5"), False)

def remove_consecutive_duplicates2(s):
    a = s.split()
    acc=[]
    for i,x in enumerate(a):
        if i < len(a)-1 :
            if x != a[i+1]:
                acc.append(x)
        if i == len(a)-1 :
            if x != a[i-1]:
                acc.append(x)
    return ' '.join(acc)

# use itertool and groupby
from itertools import groupby

def remove_consecutive_duplicates(s):
    return ' '.join(k for k,_ in groupby(s.split()))
# groupby example
# >>> [k for k,g in groupby('AAABBCCCCCCCDDDDEE')]
# ['A', 'B', 'C', 'D', 'E']

#print(remove_consecutive_duplicates('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'))
#print('alpha beta gamma delta alpha beta gamma delta')

def initials2(name):
    names = name.split()
    initName = ''
    for i, na in enumerate(names):
        if(i == len(names)-1):
            initName+=(names[i].capitalize())
        else:
            initName+=(names[i][0:1]).upper() + '.'
    return initName
# clever solution
def initials(name):
    names = name.split()
    print([x[0].upper() for x in names]) #Capitalize first letter of all the subnames
    print(names[-1].capitalize())
    return '.'.join(x[0].upper() for x in names[:-1]) + '.'+ names[-1].capitalize()

# print(initials('code wars'),'C.Wars')
# print(initials('Barack hussein obama'),'B.H.Obama')
# print(initials('barack hussein Obama'),'B.H.Obama')

def remove_duplicate_words2(s):
    rem = ''
    for x in s.split(' '):
        if x not in rem :
            rem += x + ' '
    return rem.strip()

#dict and from key
def remove_duplicate_words(s):
    return(' '.join(dict.fromkeys(s.split())))

#print(remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta") )
#print("alpha beta gamma delta")
#print(remove_duplicate_words("my cat is my cat fat"))
#print("my cat is fat")

#my humble solution
def eight_bit_number1(n):
    print([n])
    if re.match(r'\d{1,3}', n) == None : 
        return False
    if n == '':
        return False
    if int(n) <=255 and int(n)>=0:
        if len(n) > 1 and n[0]=='0' :
            return False
        return True
    else:
        return False

import re
def eight_bit_number(n) : # < 256
    print([n])
    return bool(re.fullmatch(r'0|[1-9]\d?|1\d+|2[0-4]\d|25[0-5]', n))

#tests = [
##    ("",    False),
#    ("0",   True),
#    ("00",  False),
#    ("1\n",  True),
#    ("1 ", False),
#    ("123", True),
#    ("255", True),
#    ("256", False),
#    ("999", False),
#    ("-1",  False)
#]
#
#for s, expected in tests:
#    print(eight_bit_number(s), expected)

#######################################################
#######Regexp Basics - is it a six bit unsigned number?
########################################################
# Implement String#six_bit_number?, 
# which should return true if given object is a number 
# representable by 6 bit unsigned integer (0-63), false otherwise.

# It should only accept numbers in canonical representation, 
# so no leading +, extra 0s, spaces etc.
import re
def six_bit_number(n):
    print([n])
    return bool(re.fullmatch(r'[0-9]|[1-5]\d|6[0-3]',n))
     
#
#tests = [
#    ("", False),
#    ("0", True),
#    ("00", False),
#    ("55", True),
#    ("63", True),
#    ("64", False),
#    ("-0", False),
#    ("-5", False),
#    ("05", False),
#    ("5", True)
#]
#
#for s, expected in tests:
#    print(six_bit_number(s), expected)

def is_vowel1(s): 
    if len(s) > 1  or s == "":
        return False
    if s.lower() in 'aeiou' :         
        return True
    else:
        return False
# better way
## re.IGNORECASE
## re.iscape(s) ... escape special charactor
import re
def is_vowel2(s) : 
    print([s])
    return bool(re.match(r'^[aeiou]$', re.escape(s), re.IGNORECASE))

# easier way with set
def is_vowel(s):
    print([s])
    return s.lower() in set('aeiou')
#sprint(is_vowel(""), False)
#sprint(is_vowel("a"), True)
#sprint(is_vowel("E"), True)
#sprint(is_vowel("ou"), False)
#sprint(is_vowel("z"), False)
#sprint(is_vowel("lol"), False)
#sprint(is_vowel("a\n"), False)

import re
def is_letter(s) :
    print([s])
    return bool(re.match(r'^[a-zA-Z]$',re.escape(s)))

#print(is_letter(""), False)
#print(is_letter("a"),True)
#print(is_letter("X"), True)
#print(is_letter("7"), False)
#print(is_letter("*"), False)
#print(is_letter("ab"), False)
#print(is_letter("a\n"), False)

#started at 6:52
def remove_url_anchor1(url):
    if '#' in url :
        return url[0:url.index('#')]
    else :
        return url
#finished 6: 57
# clever way
def remove_url_anchor(url):
    return url.split('#')[0]

# usiung regex
## re.sub
## . matches any character except for line terminator
def remove_url_anchor(url):
    re.sub(r'#.*$', '', url)
#
#print(remove_url_anchor("www.codewars.com#about"), "www.codewars.com");
#print(remove_url_anchor("www.codewars.com/katas/?page=1#about"), "www.codewars.com/katas/?page=1")
#print(remove_url_anchor("www.codewars.com/katas/"), "www.codewars.com/katas/")



# find longest gab
# num is any sequence of consecutive zeros 
# that is surrounded by ones at both ends in the binary representation of num.
# 9 has binary representation 1001 and contains a binary gap of length 2.
# 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3.
# 20 has binary representation 10100 and contains one binary gap of length 1.
# 15 has binary representation 1111 and has 0 binary gaps.
# Write function gap(num) that,  given a positive num,  returns the length of its longest binary gap.
# The function should return 0 if num doesn't contain a binary gap.
# start 7:07
def gap2(num):
    b = (str(bin(num))[2:])
    idx = [m.start() for m in re.finditer(r'1', b)]
    print('binary ', b, 'idx', idx)
    i = len(idx) -1
    maxlen = 0
    while i > 0 :
        print('i=', i, idx[i], idx[i-1])
        maxlen =( max(idx[i] - idx[i-1] -1 , maxlen))
        i-=1

    return maxlen
# finished at  7:32j took 25 min

## clever way 
## map
## strip
## split
def gap(num):    
    striped = bin(num)[2:].strip("0") #remove 0 at front and rear
    print(striped, '==> split("1")', striped.split("1"))
    return max(map(len, striped.split('1')))
#best way

#print(gap(9), 2)
#print(gap(529),4)
#print(gap(20),1)
#print(gap(15),0)

# rules
# at least 1 uppercase letter.
# at least 1 lowercase letter.
# at least 1 number.
# be at least 8 characters long.
## must contain Capital; : r'.*[A-Z]'
# my humble way
import re
def password(string):
    if len(string) < 8:
        return False
    if re.match(r'.*[A-Z]', string) == None :
        return False
    if re.match(r'.*[a-z]' ,string )== None : 
        return False
    if re.match(r'.*\d', string) == None:
        return False
    return True

# clever way
## for in criteria
## all(any(map(f, s))) for
## BEST solution
CRITERIA = (str.islower, str.isupper, str.isdigit)
def password2(s):
    return len(s) >= 8 and all(any(map(x, s))  for x in CRITERIA)


## pure regex
def password(s):
    return bool(re.match(r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}',s))

#print(password("Abcd1234"), True)
#print(password("Abcd123"), False)
#print(password("abcd1234"), False)
#print(password("AbcdefGhijKlmnopQRsTuvwxyZ1234567890"), True)
#print(password("ABCD1234"), False)
#print(password("Ab1!@#$%^&*()-_+={}[]|\:;?/>.<,"), True)
#print(password("!@#$%^&*()-_+={}[]|\:;?/>.<,"), False)
#print(password(""), False)
#print(password(" aA1----"), True)
#print(password("4aA1----"), True)

#count "Sand", "Water", "Fish", and "Sun" without overlapping 

def sum_of_a_beach1(beach):
    objs = ["sand", "water", "fish", "sun"]
    cnt=0
    beach = beach.lower()
    for o in objs:
        if o in beach :
            ocnt = beach.count(o)
            cnt+=ocnt    
    return cnt
# finished 8:56

#with regex
def sum_of_a_beach(beach):
    return len(re.findall(r'sand|water|fish|sun', beach, re.IGNORECASE))

# with for statement
## sum(string.count() for)
def sum_of_a_beach(beach):
    return sum(beach.lower().count(x) for x in ["sand", "water", "fish", "sun"])

## sum for _  finditer
def sum_of_a_beach(beach):
    return sum(1 for _ in re.finditer(r'sand|water|fish|sun', beach.lower()))

# print(sum_of_a_beach("SanD"), 1)
# print(sum_of_a_beach("sunshine"), 1)
# print(sum_of_a_beach("sunsunsunsun"), 4)
# print(sum_of_a_beach("123FISH321"), 1)

# finished 9:28
def remove_special_char(name):
    return re.sub(r'[%$&/£\?@\d]', '', name).upper()

#print(remove_special_char("k?%35a&&/y@@@£5599 m93753&$$$c$n///79u??@@%l?975$t?%5y%&$3$1!"), 'KAY MCNULTY!')
#print(remove_special_char("9?9?9?m335%$£@a791%&$r$$$l£@53$&y&n%$5@ $£5577w&7e931%s$£c$o%%%f351f??%!%%"), 'MARLYN WESCOFF!')
#print(remove_special_char("%&$557f953//1/$£@%r%935$$£a@£3111$@???%n???5 $%157b%///$i%55&31£@l?%&$$a%@£$s5757!$$%%%%53"), 'FRAN BILAS!')
#print(remove_special_char("///$%&£$553791£r357%??@$%u?$%@7993111£@$%t£$h3% 3$£l$311i3%@?&c3£h%&t&&?%11e%$?@11957r79%£&£m$$a55n1!111%%"), 'RUTH LICHTERMAN!')
#print(remove_special_char("??£@%&a5d15??e599713%l%%e%75913 1£$%&@g@£%o&$@13l5d11s$%&t15i9n&5%%@%e@£$!£%$£"), 'ADELE GOLDSTINE!')    

# alphabetical order. space allowed, regex match
REGEX = r''

# start time : 9:35
def vowel_2_index(string):
    vo = ''
    for i, x in enumerate(string):
        if x.lower() in 'aeiou':
          vo+= str(i+1)
        else:
            vo += x
    return vo
# finished :9:54

#start time : 
## ''.join for
def vowel_2_index(string):
    return ''.join(x if x.lower() not in 'aeiou' else str(i+1) for i, x in enumerate(string))
#finishing time : 10:01

## lambda
## re.sub()
vowel_2_index = lambda st : ''.join(str(i) if x.lower() in 'aeiou' else x for i, x in enumerate(st))
#finishng time 10-19
#print(vowel_2_index('this is my string'),'th3s 6s my str15ng')
#print(vowel_2_index('Codewars is the best site in the world'),'C2d4w6rs 10s th15 b18st s23t25 27n th32 w35rld')
#print(vowel_2_index('Tomorrow is going to be raining'), 'T2m4rr7w 10s g1415ng t20 b23 r2627n29ng')
#print(vowel_2_index(''), '')
#print(vowel_2_index("90's cornhole Austin, pickled butcher yr messenger bag gastropub next level leggings listicle meditation try-hard Vice. Taxidermy gastropub gentrify, meh fap organic ennui fingerstache pickled vegan. Seitan sustainable PBR&B cornhole VHS. Jean shorts actually bitters ugh blog Intelligentsia. Artisan Kickstarter DIY, fixie cliche salvia lo-fi four loko. PBR&B Odd Future ugh fingerstache cray Wes Anderson chia typewriter iPhone bespoke four loko, Intelligentsia photo booth direct trade. Aesthetic Tumblr Portland XOXO squid, synth viral listicle skateboard four dollar toast cornhole Blue Bottle semiotics."),"90's c7rnh11l13 1516st19n, p24ckl28d b32tch36r yr m43ss46ng49r b53g g57str61p63b n67xt l72v74l l78gg81ngs l87st90cl93 m96d98t100t102103n try-h111rd V116c118. T122x124d126rmy g132str136p138b g142ntr146fy, m152h f156p 159rg162n164c 167nn170171 f174ng177rst181ch184 p187ckl191d v195g197n. S202203t205n s209st212213n215bl218 PBR&B c227rnh231l233 VHS. J241242n sh247rts 252ct255256lly b262tt265rs 269gh bl275g 278nt281ll284g286nts290291. 294rt297s299n K303ckst308rt311r D315Y, f320x322323 cl327ch330 s333lv336337 l340-f343 f346347r l351k353. PBR&B 362dd F367t369r371 373gh f378ng381rst385ch388 cr392y W396s 399nd402rs405n ch410411 typ416wr419t421r 424Ph427n429 b432sp435k437 f440441r l445k447, 450nt453ll456g458nts462463 ph467t469 b472473th d478r480ct tr486d488. 491492sth496t498c T502mblr P509rtl513nd X518X520 sq524525d, synth v536r538l l542st545cl548 sk552t554b556557rd f562563r d567ll570r t574575st c580rnh584l586 Bl590591 B594ttl598 s601m603604t606cs.")


# array containing the document IDs (1-based indices of documents in the array), where the term occurs, sorted in ascending order.
# 
# Booleans:
# 
# CaseSensitive: test matches test, but not Test
# Not CaseSensitive: test matches both test and Test
# 
# Exact Match: test matches test and .test!, but not attest or test42
# Not Exact Match: test matches both test and attest
# start 10:32
def build_inverted_index(collection, term, case_sensitive, exact_match):
    arr = []
    for i, x in enumerate(collection):
        if not case_sensitive : 
            if term.lower() in x.lower() : 
                if exact_match : 
                    x = re.sub(r'\W', ' ', x)
                    for y in x.split(' '):
                        if term.lower() ==  y.lower() : 
                            arr.append(i+1)
                else : 
                    arr.append(i+1)
        else : #case insensitive
            if term in x :
                if exact_match : 
                    x = re.sub(r'\W', ' ', x)
                    for y in x.split(' '):
                        if term ==  y : 
                            arr.append(i+1)
                else : 
                    arr.append(i+1)
    return arr
# finished 10:58
#print(build_inverted_index(['hello there', 'gEnErAl kenobi'],'general', True, False),[])
#print(build_inverted_index(['Lorem Ipsum Dolor', 'Hodor Dolor Hodor', 'Dolormiten are not a thing'],'Dolor', True, False),[1,2,3])
#print(build_inverted_index(['hello there', 'general kenobi'],'Hello', False, False),[1])
#print(build_inverted_index(['Rumpel Dumpel','Holger', 'Quadrumpel'],'UmPeL', False, False),[1,3])
#print(build_inverted_index(['hello. there', 'general kenobi'],'hello', True, True),[1])
#print(build_inverted_index(['Im Wald gibts nicht viel zu tun', 'Oooh du schoener Westerwald'],'wald', False, True),[1])
#print(build_inverted_index(['hellos there', 'general kenobi'],'Hello', False, False),[1])
#print(build_inverted_index(['hello there', 'general kenobi'],'Hello', True, False),[])
#print(build_inverted_index(['hello there', 'general kenobi'],'Hell', False, False),[1])

# 12:46
# format 01-09-2016 01:20
def date_checker(date):
    return bool(re.match(r'\d\d-\d\d-\d\d\d\d \d\d:\d\d', date))
    #your code here
#12:53

def date_checker(date):
    return bool(re.match(r'\d{2}-\d{2}-\d{4} \d{2}:\d{2}', date))


#print(date_checker("01-09-2016 01:20"), True)
#print(date_checker("01-09-2016 01;20"), False)
#print(date_checker("01_09_2016 01:20"), False)
#print(date_checker("14-10-1066 12:00"), True)
#print(date_checker("Tenth of January"), False)
#print(date_checker("20 Sep 1988"), False)
#print(date_checker("19-12-2050 13:34"), True)
#print(date_checker("Tue Sep 06 2016 01:46:38 GMT+0100"), False)
#print(date_checker("01-09-2016 00:00"), True)
#print(date_checker("01-09-2016 2:00"), False)

#start at 1:00
# removes specific strings
def remove_bmw(string):
   return ''.join(x  for x in string if x.lower() not in 'bmw')
#finish at 1:03

#print(remove_bmw("bmwvolvoBMW"), "volvo")
#print(remove_bmw("blablahblah"), "lalahlah")

def remove_chars(s):
    return re.sub(r'[^a-zA-Z ]','', s)

# print(remove_chars("test for error!"),"test for error")
# print(remove_chars(".tree1"),'tree')

#If the 3rd letter is a consonant, return the first 3 letters.
#If the 3rd letter is a vowel, return the first 4 letters.
def nickname_generator(s):
    return s[0:4] if s[2] in 'aeiou' else s[0:3]
# finished1:19

# print(nickname_generator("Jimmy"), "Jim");
# print(nickname_generator("Samantha"), "Sam");
# print(nickname_generator("Sam"), "Error: Name too short");
# print(nickname_generator("Kayne"), "Kay", "'y' is not a vowel");
# print(nickname_generator("Melissa"), "Mel");
# print(nickname_generator("James"), "Jam");

def remove_exclaime(s): #only from back
    arr = s.split(' ')
    return ' '.join(x.rstrip('!') for x in arr)
#finished 1:32        

#print(remove_exclaime('Hi!'), 'Hi')
#print(remove_exclaime('Hi!!!'),'Hi')
#print(remove_exclaime('!Hi'), '!Hi')
#print(remove_exclaime('!Hi!'), '!Hi')
#print(remove_exclaime('Hi! Hi!'), 'Hi Hi')
#print(remove_exclaime('!!!Hi !!hi!!! !hi') , '!!!Hi !!hi !hi')

# validate phone number British version
#  begin with '07' followed by 9 other digits, e.g. '07454876120'.
# sometimes the number is preceded by the country code, 
# the prefix '+44', which replaces the '0' in ‘07’, e.g. '+447454876120'
# And sometimes you will find numbers with dashes in-between digits or on either side, 
# e.g. '+44--745---487-6120' or '-074-54-87-61-20-'. As you can see, dashes may be consecutive.

def validate_number(string):
    number =  re.sub(r'[+-]', '', string)
    print(number)
    if (re.match(r'07\d{9}$', number)) != None : 
        return "In with a chance"
    elif re.match(r'447\d{9}$', number) != None:
        return 'In with a chance"'
    else:
        return "Plenty more fish in the sea"


#regex is the weakest area
## do it again later
import re
yes = "In with a chance"
no = "Plenty more fish in the sea"
def validate_number(string):
  return yes if re.match(r'^(\+44|0)7[\d]{9}$',re.sub('-','',string)) else no\

#print(validate_number("07454876120"), "In with a chance")
#print(validate_number("0754876120"), "Plenty more fish in the sea")
#print(validate_number("0745--487-61-20"), "In with a chance")
#print(validate_number("+447535514555"), "In with a chance")
#print(validate_number("-07599-51-4555"), "In with a chance")
#print(validate_number("075335440555"), "Plenty more fish in the sea")
#print(validate_number("+337535512555"), "Plenty more fish in the sea")
#print(validate_number("00535514555"), "Plenty more fish in the sea")
#print(validate_number("+447+4435512555"), "Plenty more fish in the sea", "Not a Briish prefix")
#print(validate_number("+44"), "Plenty more fish in the sea", "Not a Briish prefix")


#start at 9:10
# add up each date, month, year and sum respectively until <10
def life_path_number(birth):
    y,m, d = birth.split('-')
    while (int(y) > 10):
        y = sum(int(x) for x in (list(str(y))))
    while(int(m)>10):
        m = sum(int(x) for x in (list(str(m))))
    while(int(d)>10):
        d = sum(int(x) for x in (list(str(d))))
    s = int(y) + int(m) +int(d)
    while(s >= 10) :
        s = sum(int(x) for x in (list(str(s))))
    return s    
#finished at 9:37    
# clever way
## string.replace()
def life_path_number(date):
    return int(date.replace('-', '')) % 9 or 9

#print(life_path_number("1955-10-28"), 4)
#print(life_path_number("1971-06-28"), 7)

# start at 09:51
def validate_time(time):
    return bool(re.match(r'(1\d|2[0-3]|0?\d):[0-5][0-5]', time))
# finished at 10:05

    #your code here
#print(validate_time('1:00'), True)
#print(validate_time('1:00'), True)
# print(validate_time('13:1'), False)
# print(validate_time('12:60'), False)
# print(validate_time('12: 60'), False)
# print(validate_time('24:00'), False)
# print(validate_time('00:00'), True)
# print(validate_time('24o:00'), False)
# print(validate_time('24:000'), False)
# print(validate_time(''), False)
# print(validate_time('09:00'), True)
# print(validate_time('2400'), False)
# print(validate_time('foo12:00bar'), False)
# print(validate_time('010:00'), False)
# print(validate_time('1;00'), False)

# time started 10:16
import re
def ipValidator2(ip):
    print([ip])
    valid = True
    if len(ip.split('.') ) != 4  or ' ' in ip: 
        return False
    for x in ip.split('.') :
        try : 
            if int(x) > 255:
                valid = False
                return valid
        except : 
            return 'False'
    return valid
#10:44
# regex

def ipValidator(ip):
    if (re.match(r'^(\d{1,3}\.){3}(\d{1,3})$', ip)) :
        for each in ip.split('.') : 
             if int(each) > 255 : 
                 return False
        return True
    else:
        return False
  
# print(ipValidator('123.456.789.0'))
# print(ipValidator('127.0.0.1') == True,'\"127.0.0.1\" is valid IP')
# print(ipValidator('123.456.789.0') == False,'\"123.456.789.0\" is invalid IP')
# print(ipValidator('12.b.3.a'))
# print(ipValidator('12.34.56'))
# print(ipValidator(('')))
# print(ipValidator(' 1.2.3.4') )#공백처리
# print(ipValidator('1.2.3.4 '))

#given index i'th number 보다 크면서 제일 작은 least larger  번호 구하기
# tag remover

#tag remover
from re import sub
reg2 = r'</?[\w\s\#\'\"= \.]+\/?>'

# clever solution
reg = r'<[^>]*>' # <> 사이에 >제외한 모든 것 매치
reg = r'<.*?>'
#12:08
#print(sub(reg, "", "<div>test</div>"), "test");
#print(sub(reg, "", "<a href='#'>go to <b>start</b> page</a>"), "go to start page")
#print(sub(reg, "", "aaabbb<i>sss</i>zzz<hr/>vvv<hr /><br/>"), "aaabbbssszzzvvv")
#print(sub(reg, "", "<img src='home.jpg'/>foto description"), "foto description")
#print(sub(reg, "", "<p>first section<b>bold text</b>second part    </p>"), "first sectionbold textsecond part    ")
#print(sub(reg, "", "<div>text\ntext <span>2</span></div>"),"text\ntext 2")
#print(sub(reg, "", "<html lang = 'pl' ><body>content of body ... </body> ... </html>"), "content of body ...  ... ")
#print(sub(reg, "", "<div><span></span></div>"),"")
#print(sub(reg, "", ""),"")
#print(sub(reg, "", "a"),"a")
# 

# # start 12:11
def validate_time(time): #this is better
    return bool(re.match(r'(2[0-3]|[01]?\d):[0-5]\d$', time))
# def validate_time(time):
#     return bool(re.match(r'(([0-1]\d|2[0-3])|\d)(:[0-5]\d)', time))
# print(validate_time('1:00'), True)
# print(validate_time('1:00'), True)
# print(validate_time('13:1'), False)
# print(validate_time('12:60'), False)
# print(validate_time('12: 60'), False)
# print(validate_time('24:00'), False)
# print(validate_time('00:00'), True)
# print(validate_time('24o:00'), False)
# print(validate_time('24:000'), False)
# print(validate_time(''), False)
# print(validate_time('09:00'), True)
# print(validate_time('2400'), False)
# print(validate_time('foo12:00bar'), False)
# print(validate_time('010:00'), False)
# print(validate_time('1;00'), False)

# accept only alphabet + space
# my digging is not worth record it
# is this best solution
def nothing_special(s):
    try:
        return re.sub('[^a-z0-9\s]', '', s, flags=re.IGNORECASE)
    except:
        return 'Not a string!'
#print(nothing_special("Hello World!"), "Hello World")
#print(nothing_special("%^Take le$ft ##quad%r&a&nt"), "Take left quadrant")
#print(nothing_special("M$$$$$$$y ally!!!!!"), "My ally")
#print(nothing_special(25), "Not a string!")


# get first python developer signed up
# < firstName here >, < country here > of the first Python developer who has signed up
def get_first_python3(users):
    user = ''
    for d in users:
        if d['language'] == 'Python':
            user += d["first_name"] + ", "+ d["country"]
            break
    if user == '' : 
        return "There will be no Python developers"
    return user

# look at this beautiful solution I feel frustrating comparing mine
def get_first_python2(users):
    return next(('{}, {}'.format(d['first_name'],d['country']) for d in users if d['language'] == 'Python'),'There will be no Python developers')

## format 
def get_first_python1(users) :
    for d in users :
        if d['language'] == 'Python':
            return '{}, {}'.format(d['first_name'], d['country'])

##  merge for with if
## next( (iter for in if ), 'default') 
# def get_first_python(users) :
#     if users == '':
#         return 'There will be no Python developers'
#     return next(('{}, {}'.format(d['first_name'], d['country']) for d in users if d['language'] == 'Python'), 'There will be no Python developers')
# list1 = [
#   { "first_name": "Mark", "last_name": "G.", "country": "Scotland", "continent": "Europe", "age": 22, "language": "JavaScript" },
#   { "first_name": "Victoria", "last_name": "T.", "country": "Puerto Rico", "continent": "Americas", "age": 30, "language": "Python" },
#   { "first_name": "Emma", "last_name": "B.", "country": "Norway", "continent": "Europe", "age": 19, "language": "Clojure" }
# ]

# list2 = [
#   { "first_name": "Kseniya", "last_name": "T.", "country": "Belarus", "continent": "Europe", "age": 29, "language": "JavaScript" },
#   { "first_name": "Amar", "last_name": "V.", "country": "Bosnia and Herzegovina", "continent": "Europe", "age": 32, "language": "Ruby" }
# ]

# list3 = [
#   { "first_name": "Sofia", "last_name": "P.", "country": "Italy", "continent": "Europe", "age": 41, "language": "Clojure" },
#   { "first_name": "Jayden", "last_name": "P.", "country": "Jamaica", "continent": "Americas", "age": 42, "language": "JavaScript" },
#   { "first_name": "Sou", "last_name": "B.", "country": "Japan", "continent": "Asia", "age": 43, "language": "Python" },
#   { "first_name": "Rimas", "last_name": "C.", "country": "Jordan", "continent": "Asia", "age": 44, "language": "Java" }
# ]

# print(get_first_python(list1), "Victoria, Puerto Rico")
# print(get_first_python(list2), "There will be no Python developers")
# print(get_first_python(list3), "Sou, Japan")
# print(get_first_python(list1+list3), "Victoria, Puerto Rico")
# print(get_first_python(list3+list1), "Sou, Japan")

# decode returned list of ls -l of linux
def linux_type(file_attribute):
    filetype={
        '-':'file',
        'D':'door',
        's':'socket',
        'l':'symlink',
        'p': 'pipe',
        'b':'block_file',
        'c': 'character_set',
        'd': 'directory'
    }
    return filetype[file_attribute[0]]
#
#print(linux_type("-rwxrwxrwx"),"file")
#print(linux_type("Drwxr-xr-x"),"door")
#print(linux_type("lrwxrw-rw-"),"symlink")
#print(linux_type("srwxrwxrwx"),"socket")
#
#finished at 2:16

#rule :  8 - 20 characters
# t least one character from each category): 
# uppercase letters, lowercase letters, digits, 
# and the special characters !@#$%^&*?
#gaveup source
# best solution
import re;
def check_password(s):
    if re.search('^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?\d)(?=.*?[!@#$%^&*?])[a-zA-Z\d!@#$%^&*?]{8,20}$', s) :
        return 'valid'
    else:
        return 'not valid'

# another one
def check_password(s):
    m = re.match(r'(?=.{8,20}$)(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*?])(?=^[a-zA-Z\d!@#$%^&*?]*$)', s)
    return 'valid' if m else 'not valid'

# maybe this is more understandable
import re

PATTERN = re.compile(
'^'                   # begin string
'(?=.*?[A-Z])'        # at least one uppercase letter
'(?=.*?[a-z])'        # at least one lowercase letter
'(?=.*?\d)'           # at least one digit
'(?=.*?[!@#$%^&*?])'  # at least one special character
'[A-Za-z\d!@#$%^&*?]' # only the given characters
'{8,20}'              # between 8 and 20 characters long
'$'                   # end string
)

def check_password(s):
    return "valid" if PATTERN.match(s) else "not valid"

def check_password(string):
    reduced = sub("[a-z]", "a", sub("[A-Z]", "A", sub("[0-9]", "0", sub("[!@#$%^&*?]", "!", string))))
    return "valid" if 8 <= len(string) <= 20 and set(reduced) == set("aA0!") else "not valid"

#another one
def check_password(s):
    c1 = 8 <= len(s) <=20
    c2 = any([i.isupper() for i in s])
    c3 = any([i.islower() for i in s])
    c4 = any([i.isdigit() for i in s])
    c5 = any([i for i in s if i in '!@#$%^&*?'])
    c6 = not any([i for i in s if i not in '!@#$%^&*?' and not i.isupper() and not i.islower() and not i.isdigit()])
    return 'valid' if c1 and c2 and c3 and c4 and c5 and c6 else 'not valid'

#this looks easier
import re
def check_password(s):
    if len(s) > 20 or len(s) < 8: return "not valid"
    a1 = bool(re.search(r'[A-Z]', s))
    a2 = bool(re.search(r'[a-z]', s))
    a3 = bool(re.search(r'\d', s))
    a4 = bool(re.search(r'[!@#$%^&*?]', s))
    a5 = bool(re.search(r'^[A-Za-z!@#$%^&*?\d]*$', s))
    return "valid" if a1*a2*a3*a4*a5 else "not valid"

#print(check_password(""), "not valid")
#print(check_password("password"), "not valid")
#print(check_password("P1@p"), "not valid")
#print(check_password("P1@pP1@p"), "valid")
#print(check_password("P1@pP1@pP1@pP1@pP1@pP1@p"), "not valid")
#print(check_password("Paaaaaa222!!!"), "valid")

# 7:40
def least_larger2(a, i):
    if len([k for k in a if k > a[i]]) >= 1:
        if [k for k in a if a[i]<k] ==[] :
            return -1
        return a.index(min([k for k in a if a[i] < k] ))
    else:
        return -1
def least_larger(a, i):
    larger =[ k for k in a if k> a[i]]
    return a.index(min(larger)) if larger else -1

# print(least_larger( [4, 1, 3, 5, 6], 0), 3 )
# print(least_larger( [4, 1, 3, 5, 6], 4), -1 )
# print(least_larger([0,0], 1),-1)
# print(least_larger([1, 2, 3, 4, 5, 0], 3),4)
#8:01

#8:19
#list in between duplicate element 
def duplicate_sandwich(arr):
    dup = {}
    sandwitch = []
    found = 0 
    for i, k in enumerate(arr) :
        print(i, k)
        if arr.count(k) == 2 :
            found +=1
            print('dup :', i, k)
        if(found > 1 and found < 2 ) :
            sandwitch.append(k)
    return sandwitch

print(duplicate_sandwich([0, 1, 2, 3, 4, 5, 6, 1, 7, 8]), [2, 3, 4, 5, 6])
print(duplicate_sandwich(['None', 'Hello', 'Example', 'hello', 'None', 'Extra']), ['Hello', 'Example', 'hello'])
print(duplicate_sandwich([0, 0]), [])
print(duplicate_sandwich([True, False, True]), [False])
print(duplicate_sandwich(['e', 'x', 'a', 'm', 'p', 'l', 'e']), ['x', 'a', 'm', 'p', 'l'])