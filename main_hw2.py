def func(*args, **kwargs):  # am folosit si kwargs intrucat avem un param key:value in cerinta de la ultimul print
    el_sum = 0
    val_sum = 0
    for i in args:
        if type(i) == int or type(i) == float:
            el_sum += i
    for k in kwargs.values():  # pot adauga sau nu param key:value
        if type(k) == int or type(k) == float:
            val_sum += k
    return el_sum  # + val_sum


def adun_n(n):
    if n == 0:
        return 0
    return n + adun_n(n - 1)


def adun_p(n):
    if n == 0:
        return 0
    if n % 2 != 0:
        return adun_p(n - 1)
    return n + adun_p(n - 1)


def adun_i(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return adun_i(n - 1)
    return n + adun_i(n - 1)


def sume(n):
    print(f'Suma nr de la 0 l la {n} este: ', adun_n(n))
    print(f'Suma nr pare de la 0 l la {n} este: ', adun_p(n))
    print(f'Suma nr impare de la 0 l la {n} este: ', adun_i(n))


print(sume(8))


def ret_int():
    n = input('Introduceti un nr:')
    if n[0] in ['+', '-']:
        sign = n[0]
        n = n.removeprefix('-')
        n = n.removeprefix('+')
        if n.isdigit():
            n = sign + n
            return int(n)
        elif len(n) == 0:
            return 0
    elif n.isdigit():
        return n
    else:
        return 0


print(func())
print(func(1, 5, -3, 'abc', [12, 56, 'cad']))
print(func(2, 4, 'abc', param_1=2))

print(ret_int())


# solutia D-ului Botond: am inteles-o dar nu as fi reusit sa o fac
# am pastrat si nr initial

def tup_sum(n, s=0, p=0, i=0):
    if n == 0:
        return 0, s, p, i
    if n % 2 == 0:
        p = p + n
    else:
        i = i + n
    rez = tup_sum(n - 1, s, p, i)
    s = n + rez[1]
    p = rez[2]
    i = rez[3]
    return n, s, p, i


print(tup_sum(8))
