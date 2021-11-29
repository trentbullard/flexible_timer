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
    print(f'({mainstarttime.astimezone().strftime("%X %p")}) main timer starting')
    intervals = [
        {
            'action': 'PREP',
            'startmessage': 'prepare steamer',
            'duration': timedelta(minutes=5)
        },
        {
            'action': 'STEAM',
            'startmessage': 'start steaming',
            'duration': timedelta(minutes=20)
        },
        {
            'action': 'VENT',
            'startmessage': 'vent steamer',
            'duration': timedelta(minutes=20)
        },
    ]
    rhythm = len(intervals)-1
    currentinterval = 0
    breakdelta = timedelta(hours=3)

    loopstarttime = datetime.now(timezone.utc)
    loopdelta = loopstarttime - mainstarttime
    lastintervaltime = loopstarttime
    interval = intervals[currentinterval]
    print(f'({loopstarttime.astimezone().strftime("%X %p")}) {interval["action"]} starting | {interval["startmessage"]}')
    ping = True
    while loopdelta < breakdelta:
        time.sleep(.05)
        loopstarttime = datetime.now(timezone.utc)
        loopdelta = loopstarttime - mainstarttime
        
        interval = intervals[currentinterval]
        timesincelastinterval = loopstarttime - lastintervaltime
        if timesincelastinterval > interval['duration']:
            winsound.Beep(400, 200)
            print("")
            print(f'({loopstarttime.astimezone().strftime("%X %p")}) {interval["action"]} completed | {intervals[currentinterval+1 if currentinterval < rhythm else 0]["startmessage"]}')
            print("")
            lastintervaltime = loopstarttime
            currentinterval = currentinterval+1 if currentinterval < rhythm else 0
            continue
        
        if loopdelta.seconds % 300 == 0:
            if ping:
                print(f'({loopstarttime.astimezone().strftime("%X %p")}) {interval["action"]} has been running for {roundsecondstd(timesincelastinterval)} | {interval["startmessage"]}')
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
