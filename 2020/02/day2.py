import os

def solve(myInput):
    valid_pwd_1 = 0
    valid_pwd_2 = 0
    for line in myInput:
        positions, character, pwd = line.split(" ")
        num1, num2 = map(int, positions.split("-"))
        char = character[0]

        if num1 <= pwd.count(char) <= num2:
             valid_pwd_1 += 1
        
        if pwd[num1 - 1] == char and pwd[num2 - 1] != char:
            valid_pwd_2 += 1
        elif pwd[num1 - 1] != char and pwd[num2 - 1] == char:
            valid_pwd_2 += 1

    print(valid_pwd_1, valid_pwd_2)
    


script_dir = os.path.dirname(__file__)
with open(script_dir + "/input", "r") as myInput:
    input = [line.replace("\n", "") for line in myInput.readlines()]
    solve(input)