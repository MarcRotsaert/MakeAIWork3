import schedule


def pyolo():
    print("yolo")


schedule.every(10).seconds.do(pyolo)
while True:
    schedule.run_pending()
    # time.sleep(1)
