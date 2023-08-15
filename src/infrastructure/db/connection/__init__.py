from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from src.infrastructure.db.connection.base import Base

# importando os elementos definidos no modelo
from src.infrastructure.db.entities.assunto_entity import AssuntoEntity
from src.infrastructure.db.entities.alternativa_entity import AlternativaEntity
from src.infrastructure.db.entities.questao_entity import QuestaoEntity

# url de acesso ao banco (essa é uma url de acesso ao sqlite local)
db_url = 'sqlite:///database/db.sqlite3'

# cria a engine de conexão com o banco
engine = create_engine(db_url, echo=False)

# Instancia um criador de seção com o banco
Session = sessionmaker(bind=engine)

# cria o banco se ele não existir
if not database_exists(engine.url):
    create_database(engine.url)

# cria as tabelas do banco, caso não existam
Base.metadata.create_all(engine)

