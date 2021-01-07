[The Challenge]

Name: Simple Programming

Can you help me? I need to know how many lines there are where the number of 0's is a multiple of 3 or the numbers of 1s is a multiple of 2. Please! Here is the file: https://mega.nz/#!7aoVEKhK!BAohJ0tfnP7bISIkbADK3qe1yNEkzjHXLKoJoKmqLys

source: https://ctflearn.com/challenge/174

[The Solution]

```bash
#! /bin/bash

echo "Start!"

COUNT=0

while read l; do
  ZEROS=${l//[^0]}
  UNS=${l//[^1]}
  
  if [[ ($((${#ZEROS} % 3)) == 0) || ($((${#UNS} % 2)) == 0) ]]
  then
    COUNT=$(($COUNT + 1))
  fi
done <data.dat

echo $COUNT

echo "END!"
```
