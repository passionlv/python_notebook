def divide(a, b):
    try:
        print(a/b)
    except Exception as exc:
        def log(exc):
            fid = open('/home/xiaopeng/tmp/logfile.txt') # missing 'w'
            #import ipdb;ipdb.set_trace()
            print(exc)
            print(exc, file=fid)
            fid.close()
        log(exc)


if __name__ == "__main__":
    divide(1,0)