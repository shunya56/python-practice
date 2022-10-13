import random


def make_sample():
    sample_list = []
    for num in range(40):
        sample_list.append(random.randint(0, 1))

    return tuple(sample_list)


if __name__ == '__main__':
    print(make_sample())
