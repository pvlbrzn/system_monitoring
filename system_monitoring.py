import json
import psutil
from functools import wraps


def save_res_json(func):
    @wraps(func)
    def func_writer():
        res_func = func()
        data = {func.__name__: res_func}
        str_data = json.dumps(data, indent=4)
        with open(f"{func.__name__}.json", "w") as file:
            file.write(str_data)
        return res_func

    return func_writer


# this skript is static version htop

class Cpu:
    def get_data(self):
        self.res_cpu = {}
        data1 = psutil.cpu_times()  # This modul outputs info about worktime CPU
        data2 = psutil.cpu_freq()  # This modul outputs info abour frequency CPU
        self.res_cpu.update(
            user_time=data1.user,
            sys_time=data1.system,
            idle_time=data1.idle,
            guest_time=data1.guest,
            current=data2.current,
        )

    def __str__(self):
        cpu_tamplate = ("|{user_time:_^16}|{sys_time:_^16}|{idle_time:_^16}|{guest_time:_^16}|{current:_^16.5}|")

        str1 = ("{:^80}").format("CPU information")
        str2 = ("|{:*^16}" * 4 + "|{:*^16}|").format(
            "user_time", "system_time", "idle_time", "guest_time", "current"
            )
        str3 = cpu_tamplate.format(**self.res_cpu)
        return (f"\n{str1}\n{str2}\n{str3}")    


class Memory:

    def get_data(self):  # This function returns information about your memory
        self.res_memory = {}
        data = psutil.virtual_memory()  # This modul outputs info about memory
        self.res_memory.update(
            total=data.total, avail=data.available, percent=data.percent, free=data.free
        )


    def __str__(self):
        memory_tamplate = "|{total:_^20}|{avail:_^20}|{percent:_^20}|{free:_^20}|"

        str1 = ("{:^80}").format("Memory information")
        str2 = ("|{:*^20}" * 3 + "|{:*^20}|").format("total_memory", "available_memory", "percentage_usage", "free_memory")
        str3 = memory_tamplate.format(**self.res_memory)
        return (f"\n{str1}\n{str2}\n{str3}")


class Network:
    def get_data(self):
        self.res_net = {}
        data = psutil.net_io_counters()  
        self.res_net.update(
            sent=data.bytes_sent, 
            recv=data.bytes_recv, 
            p_sent=data.packets_sent, 
            p_recv=data.packets_recv, 
            errin=data.errin, 
            errout=data.errout
        )

    def __str__(self):
        tamplate = "|{sent:_^14}|{recv:_^14}|{p_sent:_^14}|{p_recv:_^14}|{errin:_^14}|{errout:_^14}|"
        
        str1 = ("{:^84}").format("System-wide network In/Out statistics")
        str2 = ("|{:*^14}" * 5 + "|{:*^14}|").format(
            "bytes_sent",
            "bytes_recv",
            "packets_sent",
            "packets_recv",
            "error_In",
            "error_Out",
        )
        str3 = tamplate.format(**self.res_net)
        
        return (f"\n{str1}\n{str2}\n{str3}")


class Battary:
    def get_data(self):
        self.battary = psutil.sensors_battery()

    
    def __str__(self):
        @staticmethod
        def secs2hours(secs):  # This function converts time format
            mm, ss = divmod(secs, 60)
            hh, mm = divmod(mm, 60)
            return "%d:%02d:%02d" % (hh, mm, ss)
        
        power_left = "Battery power left = <<{}%>>".format(self.battary.percent)
        secsleft = "Time left = <<{}>>".format(secs2hours(self.battary.secsleft))
        bat_power = "Power - <<{}>>".format(self.battary.power_plugged)

        str1 = ("{:^54}").format("Battery status information")
        str2 = ("|{:<30}" + "{:>30}|").format(power_left, secsleft)
        str3 = ("|{:_^60}|").format(bat_power) 

        return (f"\n{str1}\n{str2}\n{str3}")


class Process:

    def get_data(self):
        self.res_proc = []
        for proc in psutil.process_iter(["pid", "name", "username"]):  # enumerate all processes from a module
            self.res_proc.append(proc.info)


    def __str__(self):
        
        str1 = ("{:^120}").format("***All system processes***")
        str2 = "_" * 114

        return (f'\n\n{str1}\n{str2}')


    def print_proc(self):
        for n in self.res_proc:
            output_inf = (
                "PID {pid:>5} | process name: {name:>50} | user name : {username:>22} |"
            )
            print(output_inf.format(**n))
       

def main():
    cpu = Cpu()
    cpu.get_data()
    print(cpu)

    memory = Memory()
    memory.get_data()
    print(memory)

    network = Network()
    network.get_data()
    print(network)

    battary = Battary()
    battary.get_data()
    print(battary)

    process = Process()
    process.get_data()
    print(process)
    process.print_proc()



if __name__ == "__main__":
    main()
