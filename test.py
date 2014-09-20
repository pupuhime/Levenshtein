import levenshtein


str1 = 'LCLYTHIGRNIYYGSYLYSETWNTGIMLLLITMATAFMGYVLPWGQMSFWGATVITNLFSAIPYIGTNLV'
str2 = 'EWIWGGFSVDKATLNRFFAFHFILPFTMVALAGVHLTFLHETGSNNPLGLTSDSDKIPFHPYYTIKDFLG'

# str1='sdfjsa'
# str2='sfffdsd'

str1 = 'CA'
str2 = 'ABC'


levd = levenshtein.lev(str1, str2)
print('Levenshtein Distance:', levd)

osad = levenshtein.osa(str1, str2)
print('Damerau-levenshtein distance(OSA):', osad)

dalevd = levenshtein.dalev(str1, str2)
print('Damerau-levenshtein distance:', dalevd)

