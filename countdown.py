import time
def countdown(start):
    if start.isdigit():
        start = int(start)
        while True:
            sec=(start%60)
            mint=(start//60)%60
            hrs=(start//360)%24
            if start==0:
                print("Time's up!")
                break
            print(f'\r {mint:02} mint and sec {sec:02} and hr {hrs:02}')
            time.sleep(1)
            start-=1
    else:
        print("Error")
countdown('10')
#2*60 180*60    10800\\
# op=24*60*60
