import cProfile


def func_a():
    sum(range(10000))


def func_b():
    for _ in range(500):
        func_a()


def main_program():
    for _ in range(10):
        func_b()
    sum(range(1000000))


# プロファイリングを実行
cProfile.run('main_program()')
