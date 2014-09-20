levenshtein = require './levenshtein.coffee'


str1 = 'LCLYTHIGRNIYYGSYLYSETWNTGIMLLLITMATAFMGYVLPWGQMSFWGATVITNLFSAIPYIGTNLV'
str2 = 'EWIWGGFSVDKATLNRFFAFHFILPFTMVALAGVHLTFLHETGSNNPLGLTSDSDKIPFHPYYTIKDFLG'

# str1='sdfjsa'
# str2='sfffdsd'

str1 = 'CA'
str2 = 'ABC'


levd = levenshtein.lev str1, str2
console.log 'Levenshtein Distance:', levd

osad = levenshtein.osa str1, str2
console.log 'Damerau-levenshtein distance(OSA):', osad

dalevd = levenshtein.dalev str1, str2
console.log 'Damerau-levenshtein distance:', dalevd

