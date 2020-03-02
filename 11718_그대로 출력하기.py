#0~100줄의 문자열을 랜덤으로 입력하고, 입력이 종료되면 내 프로그램을 Ctrl + Z 또는 Ctrl + D로 종료할 것

while True:
    try:
        print(input())
    except EOFError:
        break