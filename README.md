# Python Debugging with PuDB, Charles, and cProfile
Example files from my talk "Python Debugging with PuDB, Charles and cProfile"

There are three branches, one for each demo I did. You can check them out individually, or look at master which I *believe* is all the demos merged together.

### PUDB
fortune_server.py is a fortune server with a bug. Can you use PuDB to find it?

If you check out the pudb demo branch, you'll also find a sorts.py file which has a broken quicksort.
Can you debug that with PuDB? 

### Charles
run start_services.sh  or start the microservices yourself.
open Charles, and see if you can monitor the services talking to eachother when you visit localhost: 9000

You can also use Charles to look at the session files I have included, or just to monitor your browser visiting some websites

### Profiling 
I have included sorts.py which has a bubble sort and quicksort, and a profile of running both. Try running it with cprofile,
look at the human readable format. You can also look at it with something like runsnakerun, snakeviz, or convert it for qcachegrind with pyprof2calltree (available in pip)

Try profiling other python code you have, and see if you can spot any easy wins. 

Slides, links and screenshots are available here:

## Slides

https://docs.google.com/presentation/d/1Uei-yk6xpDUOmAyvfXQd_3Gabsr7cx83SWPMOsPIfes/pub

# Links to tools:

## PuDB 
Install: pip install pudb
Invoke import pudb; pudb.set_trace()

PUDB https://documen.tician.de/pudb/
Nose-PUDB (for nose testing) - https://pypi.python.org/pypi/nose-pudb


## Charles

https://www.charlesproxy.com

## Profiling

cProfile https://docs.python.org/3/library/profile.html

Using cProfile w/ pyprof2calltree and kcachegrind/qcachegrind:
https://julien.danjou.info/blog/2015/guide-to-python-profiling-cprofile-concrete-case-carbonara

on mac `brew install kcachegrind`

http://kcachegrind.sourceforge.net/html/Home.html
