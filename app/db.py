from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import time
from sqlalchemy.exc import OperationalError

DATABASE_URL = os.getenv("DATABASE_URL")

# Espera o banco subir para poder realizar a conexão
max_retries = 10
for attempt in range(max_retries):
    try:
        engine = create_engine(DATABASE_URL)
        engine.connect()
        break
    except OperationalError:
        print(f"PostgreSQL não disponível ainda... tentativa {attempt + 1} de {max_retries}")
        time.sleep(3)
else:
    raise Exception("Não foi possível conectar ao banco após várias tentativas.")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
