from typing import Generic, TypeVar, Tuple


T = TypeVar('T')


class Sample(Generic[T]):
    """
    Generic の使い方
    インスタンス生成時にクラスの型を決める
    """
    def set(self, v:T):
        self.value: T = v

    def get(self) -> T:
        return self.value


# 受け取る型クラス
T1 = TypeVar("T1")
T2 = TypeVar("T2")


class PairList(Generic[T1, T2]):
    """
    Generic の使い方2
    インスタンス生成時にクラスの型を決める
    """
    def __init__(self):
        self._ls: List[Tuple[T1, T2]] = []

    def add(self, v1: T1, v2: T2):
        self._ls.append((v1, v2))

    def get(self, i: int) -> Tuple[T1, T2]:
        return self._ls[i]


if __name__ == '__main__':
    sample = Sample[int]()
    sample.set(1)
    val = sample.get()
    print(type(val))
    
    sample.set("1")  # 警告が出る（実際はそのまま通る）
    val2 = sample.get()
    print(type(val2))


    # 型クラスの指定
    a: PairList[str, int] = PairList()
    a.add(1, "")  # ここで警告が出る
    a.add("", 12)
