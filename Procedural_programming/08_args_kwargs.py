### Args KwArgs ###

def demo_args_kwargs(*args, **kwargs):
    print("Args : ", args)
    print("KwArgs : ", kwargs)
    for key, value in kwargs.items():
        print(f"{key} : {value}")

demo_args_kwargs(10, 20, 30, 50, "test", nom="toto", age=50, email="toto@mail.com")