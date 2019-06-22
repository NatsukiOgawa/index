import numpy as np
import random

class Algo3_1():
    def __init__(self,epsilon,total_choice_t, total_arms_k):
        self.epsilon = epsilon              # パラメータ　ε > 0
        self.total_choice_t = total_choice_t    # 全体のアームの選択数　T
        self.total_arms_k = total_arms_k    # 全体のアーム数　ｋ
        return

    def initiallize(self, total_arms_k):
        each_arms_reward = []
        each_arms_reward = np.zeros(total_arms_k)
           # 各アームの期待値をゼロに初期化する
        for i in range(0, total_arms_k):    # アームに番号を振る。インデックスなので +1 しておく
            print("No." + str(i) + "")
            each_arms_reward[i] += random.random()   # i 番目のアームをn 回引いて試行する
            print("this Arm's reward = " + str(each_arms_reward[i]))
            print()
        print(each_arms_reward)
        print()
        return

    def one(self,epsilon, test_end, total_choice_t,total_arms_k):
        n = []   # 各アームに使う探索の数 その初期値
        n = np.zeros(total_arms_k)
        for i in range(0, total_arms_k):    # アームに番号を振る。インデックスなので +1 しておく
            epsilon = random.random()
            n[i] += (epsilon * total_choice_t) / total_arms_k   # i 番目のアームをn 回引いて試行する
            print("No." + str(i+1) + " " + str(n[i]) + " trials")   # n のようすをとりあえず出力してみた
            print("epsilon = " + str(epsilon))
            print(n[i] * epsilon)

            test_end += n[i]
        print()
        # test_end = int(epsilon*total_choice_t)   # 「試行」の最終回
        bonus_end = int((1 - epsilon) * total_choice_t)  # 「ボーナス」の最終回
        print("test  fase: 1" + "-" + str(test_end) + ".")
        print()
        print("earn  fase: " + str(test_end +1) + "-" + str(total_choice_t) + ".")
        return

    def two(self, test_end, total_choice_t, total_arms_k):
        reward = []
        for i in range(test_end+1, total_choice_t + 1):

            x = i   # TODO: x：一時的な添字
        print("total fase: " + str(total_choice_t) + " times.")    # TODO: 「活用」が終了する時期 t
        return

epsilon = random.random()              # パラメータ　ε > 0
total_choice_t = 1500   # 全体のアームの選択数　T
total_arms_k = 50   # 全体のアーム数　ｋ
test_end = 0

a = Algo3_1(epsilon, total_choice_t, total_arms_k)    # Algo3_1(epsilon,total_choice_t, total_arms_k, each_arms_reward,test_end, bonus_end)
a.initiallize(total_arms_k)   # initiallize(total_arms_k)
a.one(epsilon, test_end, total_choice_t, total_arms_k)   # one(epsilon, total_choice_t, total_arms_k)
a.two(test_end,total_choice_t, total_arms_k)      # two(test_end, total_choice_t)
