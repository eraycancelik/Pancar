from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

# Create a SQLite database file
database_dir = os.path.join(os.getcwd(), "db")
app_database = os.path.join(database_dir, "pancar.db")

engine = create_engine("sqlite:///" + app_database, echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Engine_db:
    class Engine(Base):
        __tablename__ = "engines"
        id = Column(Integer, primary_key=True)
        engine_name = Column(String)
        speed = Column(String)
        torque = Column(String)

    def __init__(self, engine_name=None, speed=None, torque=None):
        self.engine_name = engine_name
        self.speed = speed
        self.torque = torque

    def create_engine(self):
        new_engine = self.Engine(
            engine_name=self.engine_name, speed=self.speed, torque=self.torque
        )
        session.add(new_engine)
        session.commit()
        session.close()

    def delete_engine(self, engine):
        new_engine = session.query(self.Engine).filter_by(engine_name=engine).first()
        session.delete(new_engine)
        session.commit()
        session.close()
        
    def get_engines(self):
        engine_list=session.query(self.Engine.engine_name)
        return engine_list
    
    def get_specific_engine(self,engine_name):
        engine=session.query(self.Engine).filter(self.Engine.engine_name==engine_name).first()
        return engine

class Gearbox_db:
    class Gearbox(Base):
        __tablename__ = "gearboxes"
        id = Column(Integer, primary_key=True)
        gearbox_name = Column(String)
        gear_ratio_list = Column(String)
        differential_gear_ratio = Column(Float)
        powertrain_efficiency = Column(Float)

    def __init__(
        self,
        gearbox_name=None,
        gear_ratio_list=None,
        differential_gear_ratio=None,
        powertrain_efficiency=None,
    ):
        self.gearbox_name = gearbox_name
        self.gear_ratio_list = gear_ratio_list
        self.differential_gear_ratio = differential_gear_ratio
        self.powertrain_efficiency = powertrain_efficiency

    def create_gearbox(self):
        new_gearbox = self.Gearbox(
            gearbox_name=self.gearbox_name,
            gear_ratio_list=self.gear_ratio_list,
            differential_gear_ratio=self.differential_gear_ratio,
            powertrain_efficiency=self.powertrain_efficiency,
        )
        session.add(new_gearbox)
        session.commit()
        session.close()

    def delete_gearbox(self, gearbox):
        new_gearbox = (
            session.query(self.Gearbox).filter_by(gearbox_name=gearbox).first()
        )
        session.delete(new_gearbox)
        session.commit()
        session.close()
        
    def get_gearboxes(self):
        gearbox_list=session.query(self.Gearbox.gearbox_name)
        # query = session.query(self.Gearbox).filter_by(gearbox_name=self.gearbox_name).first()
        return gearbox_list
    
    def get_specific_gearbox(self,gearbox_name):
        gearbox=session.query(self.Gearbox).filter(self.Gearbox.gearbox_name==gearbox_name).first()
        return gearbox

class Environment_db:
    class Environment(Base):
        __tablename__ = "environments"
        id = Column(Integer, primary_key=True)
        environment_name = Column(String)
        wind_speed = Column(Float)
        slope_angel_road = Column(Float)
        air_density = Column(Float)
        gravitational_force = Column(Float)

    def __init__(
        self,
        environment_name=None,
        wind_speed=None,
        slope_angel_road=None,
        air_density=None,
        gravitational_force=None,
    ):
        self.environment_name = environment_name
        self.wind_speed = wind_speed
        self.slope_angel_road = slope_angel_road
        self.air_density = air_density
        self.gravitational_force = gravitational_force

    def create_environment(self):
        new_environment = self.Environment(
            environment_name=self.environment_name,
            wind_speed=self.wind_speed,
            slope_angel_road=self.slope_angel_road,
            air_density=self.slope_angel_road,
            gravitational_force=self.gravitational_force,
        )
        session.add(new_environment)
        session.commit()
        session.close()

    def delete_environment(self, environment):
        new_environment = (
            session.query(self.Environment)
            .filter_by(environment_name=environment)
            .first()
        )
        session.delete(new_environment)
        session.commit()
        session.close()
        
    def get_environments(self):
        environment_list=session.query(self.Environment.environment_name)
        return environment_list

    def get_specific_environment(self,environment_name):
        environment=session.query(self.Environment).filter(self.Environment.environment_name==environment_name).first()
        return environment

class Vehicle_db:
    class Vehicle(Base):
        __tablename__ = "vehicles"
        id = Column(Integer, primary_key=True)
        vehicle_name = Column(String)
        vehicle_mass = Column(Float)
        c_aero = Column(Float)
        af_projection_area = Column(Float)
        rolling_resistance = Column(Float)
        r_dynamic_rolling = Column(Float)

    def __init__(
        self,
        vehicle_name=None,
        vehicle_mass=None,
        c_aero=None,
        af_projection_area=None,
        rolling_resistance=None,
        r_dynamic_rolling=None,
    ):
        self.vehicle_name = vehicle_name
        self.vehicle_mass = vehicle_mass
        self.c_aero = c_aero
        self.af_projection_area = af_projection_area
        self.rolling_resistance = rolling_resistance
        self.r_dynamic_rolling = r_dynamic_rolling

    def create_vehicle(self):
        new_vehicle = self.Vehicle(
            vehicle_name=self.vehicle_name,
            vehicle_mass=self.vehicle_mass,
            c_aero=self.c_aero,
            af_projection_area=self.af_projection_area,
            rolling_resistance=self.rolling_resistance,
            r_dynamic_rolling=self.r_dynamic_rolling,
        )
        session.add(new_vehicle)
        session.commit()
        session.close()

    def delete_vehicle(self, vehicle):
        new_vehicle = (
            session.query(self.Vehicle).filter_by(vehicle_name=vehicle).first()
        )
        session.delete(new_vehicle)
        session.commit()
        session.close()
    
    def get_vehicles(self):
        environment_list=session.query(self.Vehicle.vehicle_name)
        return environment_list

    def get_specific_vehicle(self,vehicle_name):
        vehicle=session.query(self.Vehicle).filter(self.Vehicle.vehicle_name==vehicle_name).first()
        return vehicle
    
# Create the table in the database
Base.metadata.create_all(engine)
