import psutil


def cpu_info():
    res = {}
    data1 = psutil.cpu_times()
    data2 = psutil.cpu_count()
    data3 = psutil.cpu_freq()
    res.update(user_time=data1.user, 
               sys_time=data1.system, 
               idle_time=data1.idle, 
               guest_time=data1.guest,
               #ctx=data2.ctx_switches,
               current=data3.current)
    
    return res


def show(cpu=None):
    cpu_sample = ("|{:*^15}"*4 + "|{:*^15}|").format("user_time", 
                                        "system_time",
                                        "idle_time",
                                        "guest_time",
                                        #"ctx_switches",
                                        "current") 
    cpu_tamplate = "|{user_time:_^15}|{sys_time:_^15}|{idle_time:_^15}|{guest_time:_^15}|{current:_^15.3}|"  
    print(cpu_sample)
    print(cpu_tamplate.format(**cpu))


def main():
    cpu_data = cpu_info()
    show(cpu=cpu_data)


if __name__ == "__main__":
    main()