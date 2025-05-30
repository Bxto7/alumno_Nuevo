import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Crear carpeta "data" si no existe, para guardar el archivo db.sqlite de forma segura
db_folder = os.path.join(os.getcwd(), "data")
os.makedirs(db_folder, exist_ok=True)

# Ruta del archivo de base de datos
db_path = os.path.join(db_folder, "db.sqlite")

# Crear motor con SQLite usando ruta segura
engine = create_engine(f"sqlite:///{db_path}", echo=False)

# Crear session y base declarativa
Session = sessionmaker(bind=engine)
Base = declarative_base()
