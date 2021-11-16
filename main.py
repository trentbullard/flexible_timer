try:
    import sys
    import traceback
    import time
    from datetime import datetime, timedelta, timezone
    from functools import reduce
    import winsound
except ImportError as err:
    print(f"couldn't load module: {err}")
    sys.exit(2)


# def argInfo():
#     print("none")


def roundsecondsdt(dt):
    some = 'thing'


def roundsecondstd(td):
    if td.microseconds < 500_000:
        return timedelta(seconds=td.seconds)
    else:
        return timedelta(seconds=td.seconds+1)


def main():
    # args = sys.argv[1:]
    # if args[0] == 'help':
    #     print('none')
    #     argInfo()
    #     return
    
    mainstarttime = datetime.now(timezone.utc)
    print(f'starting timer at {mainstarttime.astimezone()}')
    intervals = [timedelta(minutes=5),timedelta(minutes=20),timedelta(minutes=60)]
    rhythm = len(intervals)
    currentinterval = 0
    breakdelta = timedelta(hours=3)

    loopstarttime = datetime.now(timezone.utc)
    loopdelta = loopstarttime - mainstarttime
    lastintervaltime = loopstarttime
    print(f'completed interval {intervals[currentinterval]} at {loopstarttime.astimezone().strftime("%X %p")} | prepare steamer')
    ping = True
    while loopdelta < breakdelta:
        time.sleep(.05)
        loopstarttime = datetime.now(timezone.utc)
        loopdelta = loopstarttime - mainstarttime
        if currentinterval >= rhythm:
            currentinterval = 0
        
        timesincelastinterval = loopstarttime - lastintervaltime
        if timesincelastinterval > intervals[currentinterval]:
            winsound.Beep(400, 200)
            print("")
            if currentinterval == 0:
                print(f'completed interval {intervals[currentinterval]} at {loopstarttime.astimezone().strftime("%X %p")} | start steaming')
            elif currentinterval == 1:
                print(f'completed interval {intervals[currentinterval]} at {loopstarttime.astimezone().strftime("%X %p")} | vent steamer')
            elif currentinterval == 2:
                print(f'completed interval {intervals[currentinterval]} at {loopstarttime.astimezone().strftime("%X %p")} | prepare steamer')
            else:
                print(f'completed interval {intervals[currentinterval]} at {loopstarttime.astimezone().strftime("%X %p")}')
            print("")
            lastintervaltime = loopstarttime
            currentinterval += 1
            continue
        
        if loopdelta.seconds % 5 == 0:
            if ping:
                print(f'current time: {loopstarttime.astimezone().strftime("%X %p")} | runtime: {roundsecondstd(loopdelta)} | current interval: {currentinterval+1} | time since last interval: {roundsecondstd(timesincelastinterval)}')
                ping = False
                loopdelta = timedelta(seconds=1)
        else:
            ping = True


if __name__ == '__main__':
    try:
        main()
        print('exiting successfully...')
    except Exception as err:
        print(f"\nUnhandled exception in main():")
        traceback.print_exc(limit=10)
