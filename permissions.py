from enum import IntFlag, auto


class OperatorPermissions(IntFlag):
    nothing = 0
    feature_a = auto()  # 1
    feature_b = auto()  # 2
    feature_c = auto()  # 4

    def has_permission_feature_a(self):
        return self.feature_a in self

    def has_permission_feature_b(self):
        return self.feature_b in self

    def has_permission_feature_c(self):
        return self.feature_c in self

    def to_int(self):
        return int(self)


if __name__ == "__main__":
    print("1========")
    permission = OperatorPermissions(3)
    print(permission.has_permission_feature_a())
    print(permission.has_permission_feature_b())
    print(permission.has_permission_feature_c())
    print(permission)
    print(permission.to_int())

    print("1========")
    permission = OperatorPermissions(7)
    print(permission.has_permission_feature_a())
    print(permission.has_permission_feature_b())
    print(permission.has_permission_feature_c())
    print(permission)
    print(permission.to_int())

    print("2========")
    #
    permission = OperatorPermissions(8)
    print(permission.has_permission_feature_a())
    print(permission.has_permission_feature_b())
    print(permission.has_permission_feature_c())
    print(permission)
    print(permission.to_int())

    print("3========")
    print(int(permission.feature_a))
    print(int(permission.feature_a) + int(permission.feature_b))

    # NOTE: エンドポイントで以下のようなデコレータを呼び出す
    # デコレータ内でログインユーザーに設定された権限と以下の引数で指定された権限を突き合わせて満たしているかチェックする
    # @permission_required(
    #     read=OperatorPermission.feature_a,
    #     write=OperatorPermission.feature_a
    # )

    # NOTE: DBには、permissionsテーブルにuse_id, read, writeの３カラムを管理するイメージ。
    # read, writeには
