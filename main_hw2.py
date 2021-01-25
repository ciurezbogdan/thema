def func(*args, **kwargs):  # am folosit si kwargs intrucat avem un param key:value in cerinta de la ultimul print
    el_sum = 0
    val_sum = 0
    for i in args:
        if type(i) == int:
            el_sum += i
    for k in kwargs.values():  # pot adauga sau nu param key:value
        if type(k) == int:
            val_sum += k
    return el_sum  # + val_sum


def adun_n(n):
    if n == 0:
        return 0
    else:
        return n + adun_n(n - 1)


def adun_p(n):
    if n == 0:
        return 0
    else:
        if n % 2 != 0:
            return adun_p(n - 1)
        else:
            return n + adun_p(n - 1)


def adun_i(n):
    if n == 0:
        return 0
    else:
        if n % 2 == 0:
            return adun_i(n - 1)
        else:
            return n + adun_i(n - 1)


def sume(n):
    print(f'Suma nr de la 0 l la {n} este: ', adun_n(n))
    print(f'Suma nr pare de la 0 l la {n} este: ', adun_p(n))
    print(f'Suma nr impare de la 0 l la {n} este: ', adun_i(n))


sume(8)


def ret_int():
    n = input('Introduceti un nr:')
    for i in range(0, len(n)):
        if n[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '+']:
            pass
        else:
            n = 0
            break
    n = int(n)
    return n


print(func())
print(func(1, 5, -3, 'abc', [12, 56, 'cad']))
print(func(2, 4, 'abc', param_1=2))


print(ret_int())
