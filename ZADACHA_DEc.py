Vx=int(input())
V0=int(input())
t=int(input())

def decor(acceleration):
    def wrapper():
        a=acceleration(Vx,V0,t)
        S=V0*t+a*t*t/2
        print(S)
    return wrapper


@decor
def acceleration(Vx,V0,t):
    try:
        a=(Vx-V0)/t
    except ZeroDivisionError:
        print("Нельзя")
    except ValueError:
        print("Нет")
    return a

acceleration()

