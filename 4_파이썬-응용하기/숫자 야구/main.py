from random import randint


def generate_numbers():
    numbers = []

    while True:
        num = randint(0, 9)
        if(not num in numbers):
            numbers.append(num)
        if(len(numbers) == 3):
            break

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers

def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    
    new_guess = []
    count = 1
    
    while True:
        num = int(input(f"{count}번재 숫자를 입력하세요: "))
        if(num in new_guess):
            print("중복되는 숫자입니다. 다시 입력하세요.")
        elif(num > 9 or num < 0):
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        else:
            count += 1
            new_guess.append(num)
            if(count == 4):
                break
    
    return new_guess
    
def get_score(guesses: list, solution: list):
    strike_count = 0
    ball_count = 0

    for i in range(0, 3):
        if(guesses[i] == solution[i]):
            strike_count += 1
    
    for i in guesses:
        if(i in solution):
            ball_count += 1
            
    ball_count -= strike_count

    return strike_count, ball_count

# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

while True:
    tries += 1
    
    user = take_guess()
    strike, ball = get_score(user, ANSWER)
    print(f"{strike}S {ball}B")
        
    if(strike == 3):
        break

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞히셨습니다.".format(tries))