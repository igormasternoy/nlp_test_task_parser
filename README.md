# nlp_test_task_parser

Parser prints input string param as a tree e.g:

Input string : 
```
(asciitree (sometimes you) (just (want to draw)) trees (in (your terminal)))
```

Output :
```
asciitree
 +-- sometimes
 |   +-- you
 +-- just
 |   +-- want
 |       +-- to
 |       +-- draw
 +-- trees
 +-- in
     +-- your 
         +-- terminal
```
Algorithm uses intermediate stack to form object tree and after that it recursively prints tree nodes 

To install make:
```
python setup.py sdist

cd tree_parser-0.1.0/parser

python parser.py "(asciitree (sometimes you) (just (want to draw)) trees (in (your terminal)))"
```
