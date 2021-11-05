try:
    import sys
    import traceback
    import time
    from datetime import datetime, timedelta
    from functools import reduce
except ImportError as err:
    print(f"couldn't load module: {err}")
    sys.exit(2)


# def argInfo():
#     print("none")


def main():
    # args = sys.argv[1:]
    # if args[0] == 'help':
    #     print('none')
    #     argInfo()
    #     return
    
    mainstarttime = datetime.utcnow()
    print(f'starting timer at {mainstarttime}')
    intervals = [timedelta(minutes=5),timedelta(minutes=20),timedelta(minutes=60)]
    rhythm = len(intervals)
    currentinterval = 0
    breakdelta = timedelta(hours=3)

    loopstarttime = datetime.utcnow()
    loopdelta = loopstarttime - mainstarttime
    lastintervaltime = loopstarttime
    ping = True
    while loopdelta < breakdelta:
        time.sleep(.05)
        loopstarttime = datetime.utcnow()
        loopdelta = loopstarttime - mainstarttime
        if currentinterval >= rhythm:
            currentinterval = 0
        
        timesincelastinterval = loopstarttime - lastintervaltime
        if timesincelastinterval > intervals[currentinterval]:
            print("")
            if currentinterval == 0:
                print(f'completed interval {intervals[currentinterval]} at {loopstarttime.astimezone()} | start steaming')
            elif currentinterval == 1:
                print(f'completed interval {intervals[currentinterval]} at {loopstarttime.astimezone()} | vent steamer')
            elif currentinterval == 2:
                print(f'completed interval {intervals[currentinterval]} at {loopstarttime.astimezone()} | prepare steamer')
            else:
                print(f'completed interval {intervals[currentinterval]} at {loopstarttime.astimezone()}')
            print("")
            lastintervaltime = loopstarttime
            currentinterval += 1
        
        if loopdelta.seconds % 300 == 0:
            if ping:
                print(f'current time: {loopstarttime.astimezone()} | runtime: {loopdelta} | current interval: {currentinterval+1} | time since last interval: {timesincelastinterval}')
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
