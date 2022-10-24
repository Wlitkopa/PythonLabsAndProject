
import re
import sys
import argparse
import fileinput

parser = argparse.ArgumentParser()
parser.add_argument("names", help="list of function names")
parser.add_argument("file", nargs='?', help="python script name")
parser.add_argument("--transform-comments", action='store_true', help="Option that transform multi-line comments into one line comments")
arguments = parser.parse_args()

print("sys.argv: ", sys.argv)
sys.argv.pop(0)

option = None
if sys.argv[0] == '--transform-comments':
    option = sys.argv.pop(0)
    # print("option: ", option)
    # print("Po popie opcji: ", sys.argv)
    # exit()

if len(sys.argv) == 1:
    sys.argv.append(input("Podaj plik, na którym mają być wykonane operacje: "))

arglist = sys.argv[0].split(",")

args = []

for i in range(len(arglist)):
    args.append(arglist[i].split(":"))

print("args: ", args)

sys.argv.pop(0)
print("sys.argv: ", sys.argv)
comflag = 0
delflag = 0
olc = ""

for i in range(len(sys.argv)):
    pyfile = open(f"{sys.argv[0]}", "r+")
    for j in range(len(args)):
        for line in fileinput.input(sys.argv[i]):
            changes = re.findall(r"(?<!\')" + args[j][0] + "(?!\')", line)
            if len(changes) > 0:
                pyfile.write(line.replace(line, re.sub(args[j][0], args[j][1], line)))
            else:
                # print("Wpisuję: ", line)
                pyfile.write(line.replace(line, line))
        pyfile.seek(0)
    print("Koniec zamiany argumentów")

    pyfile.seek(0)
    if option is not None:
        print("Działa opcja")

        for line in fileinput.input(sys.argv[i]):
            lm = re.match(r"^#", line)

            if lm is not None and comflag == 0:
                pyfile.write(line.replace(line, ''))
                olc += line[:-1]
                delflag = 1
                comflag = 1

            elif lm is not None and comflag == 1:
                pyfile.write(line.replace(line, ''))
                olc += line[1:-1]
                delflag = 1

            elif lm is None and comflag == 1:

                pyfile.write(line.replace(line, "        \n"))
                pyfile.write(line.replace(line, olc + "\n" + line))
                comflag = 0
                olc = ""

            elif line:
                pyfile.write(line.replace(line, line))
        else:
            if len(olc) > 0:
                pyfile.write(olc)
                break

    else:
        print("Nie podano opcji z usunięciem komentarzy wielolinijkowych")
    pyfile.close()

