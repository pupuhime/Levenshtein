'''
Created: 2014-9-17
Author: niR@github (https://github.com/hentaiPanda)
Version: 0.0.1
License: MIT


This is a straightforward implementation of Levenshitein
Distance and Damerau-Levenshtein Distance.

The code is based on the examples on the Wikipedia
You can get more infomation from
http://en.wikipedia.org/wiki/Levenshtein_distance
http://en.wikipedia.org/wiki/Damerau-Levenshtein_distance
'''


# Levenshtein Distance
lev = (str1, str2) ->
  n1 = str1.length
  n2 = str2.length
  matrix = ( ( 0 for i in [0..n1] ) for j in [0..n2] )
  for i in [1..n1]
    matrix[0][i] = i
  for j in [1..n2]
    matrix[j][0] = j
  for j in [1..n2]
    for i in [1..n1]
      cost = if str1[i-1] is str2[j-1] then 0 else 1
      elem = Math.min( matrix[j-1][i] + 1,
                       matrix[j][i-1] + 1,
                       matrix[j-1][i-1] + cost)
      matrix[j][i] = elem
  return matrix[-1..][0][-1..][0] #array.slice(-1)[0] return last elem


# Optimal string alignment distance
osa = (str1, str2) ->
  n1 = str1.length
  n2 = str2.length
  matrix = ( ( 0 for i in [0..n1] ) for j in [0..n2] )
  for i in [1..n1]
    matrix[0][i] = i
  for j in [1..n2]
    matrix[j][0] = j
  for j in [1..n2]
    for i in [1..n1]
      cost = if str1[i-1] is str2[j-1] then 0 else 1
      elem = Math.min( matrix[j-1][i] + 1,
                       matrix[j][i-1] + 1,
                       matrix[j-1][i-1] + cost)
      if (i > 1 and j > 1 and
          str1[i-2] is str2[j-1] and
          str1[i-1] is str2[j-2])
        elem = Math.min( elem,
                         matrix[j-3][i-3] + cost )
      matrix[j][i] = elem
  return matrix[-1..][0][-1..][0] #array.slice(-1)[0] return last elem


# Damerau-Levenshtein Distance
dalev = (str1, str2) ->
  n1 = str1.length
  n2 = str2.length
  max = n1 + n2
  letters = {}
  matrix = ( ( max for i in [0..n1+1] ) for j in [0..n2+1] )
  for i in [1..n1+1]
    matrix[1][i] = i - 1 
  for j in [1..n2+1]
    matrix[j][1] = j - 1 
  for j in [2..n2+1]
    temp = 1 
    for i in [2..n1+1]
      p2 = if letters[str1[i-2]] then letters[str1[i-2]] else 1
      p1 = temp
      cost = if str1[i-2] is str2[j-2] then 0 else 1
      if not cost
        temp = i
      elem = Math.min( matrix[j-1][i] + 1,
                       matrix[j][i-1] + 1,
                       matrix[j-1][i-1] + cost,
                       matrix[p2-1][p1-1] + 1 + (i-p1-1) + (j-p2-1))
      matrix[j][i] = elem
    letters[str2[j-2]] = j
  return matrix[-1..][0][-1..][0]



module.exports.lev = lev
module.exports.osa = osa
module.exports.dalev = dalev



if require.main is module
  str1='ca'
  str2='abc'
  console.log "str1 = 'ca', str2 = 'abc',
               D-L Distance is", dalev(str1, str2)