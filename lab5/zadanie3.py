import operator
import sys
import itertools
import functools

# lines = zip((line.strip('\n') for line in open(sys.argv[1], "r")), (line2.strip('\n') for line2 in open(sys.argv[2], "r")))
# lines = functools.reduce(operator.concat, lines)
# lines = (line.split() for line in lines)
# lines = functools.reduce(operator.concat, lines)
# lines = filter(lambda x: int(x) % 2 == 0, lines)

suma = len(list(
    filter(lambda x: int(x) % 2 == 0, functools.reduce(
        operator.concat, (line.split() for line in
                          functools.reduce(operator.concat,
                                           zip((line.strip('\n') for line in open(sys.argv[1], "r")), (line2.strip('\n') for line2 in open(sys.argv[2], "r")))
                                           )
                          )
        )
        )
    )
    )

print(suma)

