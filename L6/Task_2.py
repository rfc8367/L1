import time

def countdown(func):
    for i in range(3, 0, -1):
        time.sleep(1)
        print(i)
    func()


@countdown
def what_time_is_it_now():
    current_date_string = time.strftime('%H:%M')
    print(current_date_string)