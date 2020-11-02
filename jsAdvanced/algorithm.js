//4kyu
//##!! involves dictionary sort with value
//##!! converting object to dict type array to manupulate lambda
/*
Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the top-3 most occurring words, in descending order of the number of occurrences.

Assumptions:
1. caseinsensitive
A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII. (No need to handle fancy punctuation.)
Matches should be case-insensitive, and the words in the result should be lowercased.
Ties may be broken arbitrarily.
If a text contains fewer than three unique words, 
then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.*/

/*
Examples:
top_3_words("In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.")
# => ["a", "of", "on"]

top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
# => ["e", "ddd", "aa"]

top_3_words("  //wont won't won't")
# => ["won't", "wont"]
Bonus points (not really, but just for fun):
Avoid creating an array whose memory footprint is roughly as big as the input text.
Avoid sorting the entire array of unique words.*/
function topThreeWords0(text) {
    text = text.toLowerCase();
    let arr = text.split(' ')
    arr = arr.map(x=>x.replace(/[\s\/\,\.\/]/g, ''))
             .map(x=> x.replace(/(\s+\'\s+)/g, '') )
                .filter(x => x !== '' && x !== '\'')
    arr
    let cnt = {};
    arr.forEach(x => {
        if (x in cnt) {
            cnt[x] += 1
        }
        else{
            cnt[x] = 1;
        }        
    })
    arrcnt = Object.entries(cnt).sort((a, b)=>(b[1]-a[1]))
    return Object.keys(arrcnt).map(key=>arrcnt[key][0]).slice(0,3)
}

//##!! look at this clever guy
//## map.has method()
//## map.set
//## 
//##
//##
let topThreeWords1 = text => {
    let dict = new Map();
    text.replace(/[A-z']+(?=[ ]+|$)/g, match => {
        let word = match.toLowerCase();
        dict.set(word, dict.has(word) ? dict.get(word) + 1 : 1);
    });
    dict.delete("'");
    return [...dict].sort((a, b) => b[1] - a[1]).map(a => a[0]).slice(0, 3);
};

let topThreeWords = text=>{
    let dict = new Map();
    text.replace(/[A-z']+(?=[ ]+|$)/g, match=>{
        word = match.toLowerCase();
        console.log(word)
        dict.set(word, dict.has(word)? dict.get(word) + 1 : 1)
    });
    dict.delete("'")
    return [...dict].sort((a, b) => b[1] - a[1]).map(a => a[0]).slice(0,3);
}
function topThreeWords2(text) {
    let words = {}
    text.toLowerCase().replace(/([A-Za-z][A-Za-z']*)/g, match => {
      let c = words[match] || 0
      words[match] = ++c
    })
    return Object
            .keys(words)
            .sort(function(a,b){return words[b]-words[a]})
            .slice(0,3)
  }

//console.log(topThreeWords("a a a  b  c c  d d d d  e e e e e"), ['e','d','a'])
  
//console.log(topThreeWords("a a c b b"), ['a','b','c'])
  
//console.log(topThreeWords("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"),['e','ddd','aa'])
//console.log(topThreeWords("  //wont won't won't "), ["won't", "wont"])

  
//console.log(topThreeWords("  , e   .. "), ["e"])

//console.log(topThreeWords("  ...  "), [])

console.log(topThreeWords("  '  "), [])