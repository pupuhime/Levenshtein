This is a straightforward implementation of Levenshitein    
Distance and Damerau-Levenshtein Distance.   

The code is based on the examples on the Wikipedia    
You can get more infomation from   
http://en.wikipedia.org/wiki/Levenshtein_distance   
http://en.wikipedia.org/wiki/Damerau-Levenshtein_distance   


####Examples:####

```python
import levenshtein

str1 = 'CA'
str2 = 'ABC'

levd = levenshtein.lev(str1, str2)
print('Levenshtein Distance:', levd)

osad = levenshtein.osa(str1, str2)
print('Damerau-levenshtein distance(OSA):', osad)

dalevd = levenshtein.dalev(str1, str2)
print('Damerau-levenshtein distance:', dalevd)
```

```python
Levenshtein Distance: 3
Damerau-levenshtein distance(OSA): 3
Damerau-levenshtein distance: 2
```
