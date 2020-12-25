import time

class Sec:
    def __init__(self):
        pass

    def __enter__(self):
        pass

    @staticmethod
    def time_this(func): #Декоратор
        num_itr = int(input("Введите количество итераций: ", ))

        def time_time(self):
            av_t = 0
            for _ in range(num_itr):
                t0 = time.time()
                func(self)
                t1 = time.time()
                print(t1 - t0)
                av_t += (t1 - t0)
            av_t /= num_itr
            return "Среднее время выполнения цикла %.3f секунд" % av_t
        return time_time

    def __exit__(self, exp_type, exp_value, exp_tr):
        pass


class Fsec(Sec): #Функция
    @Sec.time_this
    def f(self):
        for j in range(1000000):
            pass


if __name__ == "__main__":
    with Sec():
        print(Fsec().f())
