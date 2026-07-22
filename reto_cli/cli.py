import sys
from core.create import create_challenge_file
# print(sys.argv)

info = sys.argv
size = len(info)

# for i, x in enumerate(info):
#     print(f"{i} - {x}")

if size > 2:
    comand = info[1]
    number = info[2]

    if comand == "create" and number.isdigit():
        print(create_challenge_file(int(number)))

else:
    print("Error en argumentos, recuerda: cli.py comando numero")
