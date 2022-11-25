
#  python -c "import sys; print([line for line in sys.stdin.read().split('\n')])"

#  python -c "import sys; print( list( map(lambda x: len(x), (line for line in sys.stdin.read().split('\n')))) )"

#  python -c "import sys; print( list( map(lambda x: len(x), (line.split(' ') for line in sys.stdin.read().split('\n'))) ) )"

#  python -c "import sys, itertools, functools; print( functools.reduce(lambda x, y: x + y, ( word.split(' ') for word in (line for line in sys.stdin.read().split('\n'))) ) )"

#  python -c "import sys, itertools, functools; print( list(sorted( map(lambda x: (x, len(x)), functools.reduce(lambda x, y: x + y, ( word.split(' ') for word in (line for line in sys.stdin.read().split('\n'))))), key=lambda t: t[1] )) )"

#  python -c "import sys, itertools, functools; from collections import Counter; print( Counter( list( map(lambda x: len(x), functools.reduce(lambda x, y: x + y, ( word.split(' ') for word in (line for line in sys.stdin.read().split('\n'))))) ) )  )"

# ROZWIĄZANIE:

# python -c "import sys, itertools, functools; from collections import Counter; print( dict( Counter( list( map(lambda x: len(x), functools.reduce(lambda x, y: x + y, ( word.split(' ') for word in (line for line in sys.stdin.read().split('\n'))))) ) ) ) )"
