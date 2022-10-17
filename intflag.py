from enum import IntFlag, auto


class Shift(IntFlag):
    MON = auto()  # 1
    TUE = auto()  # 2
    WED = auto()  # 4
    THU = auto()  # 8
    FRI = auto()  # 16
    SAT = auto()  # 32
    SUN = auto()  # 64

    def is_holiday(self) -> bool:
        return self is self.SAT | self.SUN

    def to_bin_list(self) -> list:
        return [int(i) for i in list('{:07b}'.format(int(self)))]


if __name__ == '__main__':
    print(int(Shift.MON))
    print(int(Shift.TUE))
    print(int(Shift.WED))
    print(int(Shift.THU))
    print(int(Shift.FRI))
    print(int(Shift.SAT))
    print(int(Shift.SUN))

    # 10進数から
    flag = Shift(16)
    print(flag)

    flag = Shift(18)
    print(flag)

    # 2進数から
    flag = Shift(0b1100000)
    print(flag)
    print(flag.is_holiday())

    flag = Shift(96)
    print(flag)
    print(flag.is_holiday())

    flag = Shift(96)
    print(flag)
    print(int(flag))
    print(bin(flag))

    flag = Shift(9)
    print(flag)
    print(int(flag))
    print(bin(flag))
    print('bin: {:07b}'.format(int(flag)))
    print(flag.to_bin_list())
