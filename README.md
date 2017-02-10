# jsoncsv
a simple python jsoncsv tool. no need for extra libraries. 

It flattens a json file into a flat structure with one line per leaf from the original json.

Note that the json order is not preserved.

Eg. 

file1.json
```json
{
  "a": [
    { 
      "b": 1 
    },
    { 
      "c1": 2, 
      "c2": 3, 
      "c3": { "hi": "there" }
     },
     {
       "d": [
        "d1",
        "d2"
       ]
     }
   ],
   "d": "hi"
}    
```

```sh
cat file1.json | jsoncsv |sort 
```

should generate:
```
a#0/b: 1
a#1/c1: 2
a#1/c2: 3
a#1/c3/hi: there
a#2/d#0: d1
a#2/d#1: d2
d: hi
```

where indexes are separated by a hash(#), path elements are separated by a slash(/) and the final leaf is separated by a colon and space(: )

Another way to call the script is passing a file to it:

```sh
jsoncsv file1.json |sort 
```

The only extra parameter it takes, will generate the output in a format that needs some regex escaping for greping the output:

both lines are equivalent:
```sh
cat file1.json |jsoncsv --iso |sort 
jsoncsv file1.json --iso |sort 
```

should generate:
```
a[0].b: 1
a[1].c1: 2
a[1].c2: 3
a[1].c3.hi: there
a[2].d[0]: d1
a[2].d[1]: d2
d: hi
```

where indexes are separated by brackets([]), path elements are separated by a dots(.) and the final leaf is separated by a colon and space(: )
