class SoccerPlayer(object):
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number

    def change_back_number(self, new_number):
        print("선수의 등번호를 변경합니다 : From %d to %d" % (self.back_number, new_number))
        self.back_number = new_number

    def __str__(self):
        return "Hello, My name is %s. I play in %s in center. My back number is %d " % (self.name, self.position, self.back_number)


def main():
    jinhyun = SoccerPlayer("Jinhyun", "MF", 10)
    print(jinhyun)

    print("현재 선수의 등번호는 :", jinhyun.back_number)
    jinhyun.change_back_number(5)
    print("현재 선수의 등번호는 :", jinhyun.back_number)


# 실행했을 경우에만 main() 호출
# import 한 경우에는 main() 호출 안함
if __name__ == "__main__":
    main()
