from speed_torque import Speed_Torque
from pprint import pprint

gtr = "gtr.xlsx"
ferrari = "ferrari.xlsx"
test = "test.xlsx"
engine = Speed_Torque(file=ferrari)

if __name__ == "__main__":
    try:
        
        pprint(engine.out()[0])
    except:
        print("an error occured while loading xlsx file")
