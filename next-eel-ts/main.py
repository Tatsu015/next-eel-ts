import eel


def start_eel(dev:bool):
    if dev == True:
        print('dev mode')
        dir = '../out'
        app = None
        page = {'port':3000}
    else:
        print('prod mode')
        dir = 'out'
        app = 'chrome'
        page='index.html'

    eel.init(dir)
    eel.start(page, mode=app, host='localhost', size=(1024, 768), port=8080)

if __name__ == "__main__":
    import sys
    try:
        dev = (sys.argv[1] == "dev")
    except:
        dev = False

    start_eel(dev)
