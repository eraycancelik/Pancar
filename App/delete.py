from database import Vehicle_db, Engine_db, Environment_db, Gearbox_db


gtr_engine = Engine_db()
env_1 = Environment_db()
gearset1 = Gearbox_db()
gtr_r34 = Vehicle_db()


def engine():
    try:
        gtr_engine.delete_engine(engine="test motoru (silinecek)")

    except:
        print("There is no item")


def env():
    try:
        env_1.delete_environment(environment="test ortamı silinecek")
    except:
        print("something went wrong")


def gear():
    try:
        gearset1.delete_gearbox(gearbox="test şanzımanı bu da silinecek")
    except:
        print("something went wrong")


def vehicle():
    try:
        gtr_r34.delete_vehicle(vehicle="test aracı silinecek")
    except:
        print("something went wrong")


def main():
    engine()
    env()
    gear()
    vehicle()


main()
