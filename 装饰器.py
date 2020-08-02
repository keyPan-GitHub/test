
def logger(func):
    def wrapper():
        print('logging exection')
        func()
        print('Done loggin')
    return wrapper


@logger
def sample():
    print('-- inside sample function')


if __name__ == "__main__":
    sample()