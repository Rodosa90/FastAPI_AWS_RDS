import os # libreria del sistema
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base # para manipoular la BD


#fichero = "../datos.sqlite"
# leemos el directorio actual del archivo de BD
#directorio = os.path.dirname(os.path.realpath(__file__))


# direccion BD , uniendo las 2 variables anteriores
#ruta = f"sqlite:///{os.path.join(directorio,fichero)}"


#creamos el motor 
#motor = create_engine(ruta,echo = True)

#creamos la sesion pasandole el motor
#sesion = sessionmaker(bind=motor)


#creamos Base para manejar las tablas de la BD
#base = declarative_base()


# Define la URL de conexión a tu base de datos Aurora.
# Reemplaza "username", "password", "hostname", "port" y "dbname" con los valores correctos.
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://admin:rodoapi1@fastapibd-instance-1.c7swcqemyn5x.eu-west-1.rds.amazonaws.com:3306/fastapiventas"

# Crea el motor de SQLAlchemy utilizando la URL de conexión a la base de datos Aurora.
motor = create_engine(SQLALCHEMY_DATABASE_URL)

# Crea una sesión de SQLAlchemy.
sesion = sessionmaker(bind=motor)

# Crea una instancia de Base para manipular las tablas de la base de datos.
base = declarative_base()
