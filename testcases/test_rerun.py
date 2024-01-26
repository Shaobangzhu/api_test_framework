import random

# pytest - s testcases / test_rerun.py - -reruns 5
# run 5 times

class TestMy:
    def test_my(self):
        # 生成1到3之间的随机数
        num = random.randint(1, 3)
        print("num:", num)
        if num != 1:
            print("失败")
            raise Exception("出错了")
        else:
            print("成功")