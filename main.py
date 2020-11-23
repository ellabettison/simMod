# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib.pyplot as plt
import numpy as np


def get_wq(tx, tc, tu, n):
    return (get_N(tx, tc, tu, n) / get_throughput(tx, tc, tu, n)) - get_rk(tc, tu, n)


def get_throughput(tx, tc, tu, n):
    sum = 0
    for i in range(1, n + 1):
        sum += get_pk(n, i, tx, tc, tu) * get_rk(tc, tu, i)
    # print(sum)
    return sum


def get_N(tx, tc, tu, n):
    sum = 0
    for i in range(0, n + 1):
        # print(get_pk(n, i, tx, tc, tu))
        sum += i * get_pk(n, i, tx, tc, tu)
    return sum


def get_pk(n, k, tx, tc, tu):
    prod = 1
    for i in range(0, k):
        prod *= (get_lambdak(tx, n, i) / get_rk(tc, tu, i + 1))
    return get_p0(tx, tc, tu, n) * prod


def get_p0(tx, tc, tu, n):
    sum = 0
    for i in range(1, n + 1):
        prod = 1
        for j in range(0, i):
            prod *= (get_lambdak(tx, n, j) / get_rk(tc, tu, j + 1))
        sum += prod
    # print(1/(1+sum))
    return 1 / (1 + sum)


def get_rk(tc, tu, k):
    return 1 / (tc + (k / 2) * tu)
    # return 1 / (tc + tu)


def get_lambdak(tx, n, k):
    lk =  (n - k) * (1 / tx)
    # print(lk)
    return lk


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fig, ax = plt.subplots()
    nvals = [i for i in range(1, 33)]
    wq_vals = [[],[],[]]
    speedup_vals = [[],[],[]]
    for n_ in range(1, 33):
        # tx = 100
        tc_ = 2
        tu_ = 5

        tx_ = 100
        print(get_N(tx_, tc_, tu_, n_))
        wq_vals[0].append(get_wq(tx_, tc_, tu_, n_))
        speedup_vals[0].append(n_ -get_N(tx_, tc_, tu_, n_))

        tx_ = 300
        wq_vals[1].append(get_wq(tx_, tc_, tu_, n_))
        speedup_vals[1].append(n_ - get_N(tx_, tc_, tu_, n_))

        tx_ = 500
        wq_vals[2].append(get_wq(tx_, tc_, tu_, n_))
        speedup_vals[2].append(n_ - get_N(tx_, tc_, tu_, n_))

    # ax.plot(nvals,wq_vals[0], label='tx = 100')
    # ax.plot(nvals, wq_vals[1], label='tx = 300')
    # ax.plot(nvals, wq_vals[2], label='tx = 500')
    ax.plot(nvals, speedup_vals[0], label='tx = 100')
    ax.plot(nvals, speedup_vals[1], label='tx = 300')
    ax.plot(nvals, speedup_vals[2], label='tx = 500')

    ax.set_xlabel('Number of Cores')
    ax.set_ylabel('Speedup Over a Single Core')
    ax.legend()

    ax.set_title('Speedup tx=100,300,500')
    plt.savefig('tx100300500_speedup_nok2.png')
    fig.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
