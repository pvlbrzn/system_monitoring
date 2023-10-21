import json
import psutil
from functools import wraps


def save_res_json(func):
    @wraps(func)
    def func_writer():
        res_func = func()
        with open("Function_return.json", "w") as file:
            json.dump(res_func, file, indent=4)
        res = func()
        return res

    return func_writer


@save_res_json
def cpu_info():  # This function returns information about CPU
    res = {}
    data1 = psutil.cpu_times()  # This modul outputs info about worktime CPU
    data2 = psutil.cpu_freq()  # This modul outputs info abour frequency CPU
    res.update(
        user_time=data1.user,
        sys_time=data1.system,
        idle_time=data1.idle,
        guest_time=data1.guest,
        current=data2.current,
    )
    return res


print(cpu_info())

print(cpu_info.__name__)


def show(
    cpu=None, memory=None, net=None, secs=None, charge=None, bpower=None, proc=None
):
    cpu_title = ("{:^80}").format("CPU information")
    cpu_sample = ("|{:*^16}" * 4 + "|{:*^16}|").format(
        "user_time", "system_time", "idle_time", "guest_time", "current"
    )
    cpu_tamplate = "|{user_time:_^16}|{sys_time:_^16}|{idle_time:_^16}|{guest_time:_^16}|{current:_^16.5}|"

    print("\n\n")
    print(cpu_title)
    print(cpu_sample)
    print(cpu_tamplate.format(**cpu))


def main():
    cpu_data = cpu_info()
    show(cpu=cpu_data)


if __name__ == "__main__":
    main()
