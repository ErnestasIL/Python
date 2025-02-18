from sqlalchemy import Column, create_engine, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Sukuriame duomenų bazę
engine = create_engine('sqlite:///mokykla.db')
Base = declarative_base()

# Modeliai
class Mokinys(Base):
    __tablename__ = 'mokinys'
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)
    klase = Column(Integer)

class Mokytojas(Base):
    __tablename__ = 'mokytojas'
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)
    dalykas = Column(String)

# # Sukuriame lenteles
Base.metadata.create_all(engine)
#
# # Sukuriame sesiją
Session = sessionmaker(bind=engine)
session = Session()
#
# def ar_mokinys_yra(vardas, pavarde):
#     return session.query(Mokinys).filter_by(vardas=vardas, pavarde=pavarde).first() is not None

# mokiniai = [
#     ("Jonas", "Jonaitis", 5),
#     ("Petras", "Petraitis", 6),
#     ("Asta", "Astaitė", 7),
#     ("Barbora", "Radvilaite", 10),
#     ("Kastytis", "Kerbedis", 12),
#     ("Marius", "Mclarenas", 12)
# ]
# for vardas, pavarde, klase in mokiniai:
#     if not ar_mokinys_yra(vardas, pavarde):
#         session.add(Mokinys(vardas=vardas, pavarde=pavarde, klase=klase))
#
# # Pridedame mokytojus
# mokytojai = [
#     Mokytojas(vardas="Rasa", pavarde="Rasaitė", dalykas="Matematika"),
#     Mokytojas(vardas="Bronius", pavarde="Brounas", dalykas="Istorija"),
#     Mokytojas(vardas="Kazys", pavarde="Demakovliovas", dalykas="Chemija"),
#     Mokytojas(vardas="Tomas", pavarde="Tomaitis", dalykas="Fizika")
# ]
# #
# session.add_all(mokytojai)
#
# # Išsaugome pakeitimus
# session.commit()

# Funkcija mokinių sąrašo išvedimui
def spausdinti_mokinius():
    mokiniai = session.query(Mokinys).all()
    for mokinys in mokiniai:
        print(f"{mokinys.id}. {mokinys.vardas} {mokinys.pavarde}, klasė: {mokinys.klase}")

# Funkcija mokytojų sąrašo išvedimui
def spausdinti_mokytojus():
    mokytojai = session.query(Mokytojas).all()
    for mokytojas in mokytojai:
        print(f"{mokytojas.id}. {mokytojas.vardas} {mokytojas.pavarde}, dėsto: {mokytojas.dalykas}")

def trinti_mokini_pagal_id(mokinio_id):
    mokinys = session.query(Mokinys).filter_by(id=mokinio_id).first()
    if mokinys:
        session.delete(mokinys)
        session.commit()
        print(f"Mokinys su ID {mokinio_id} buvo istrintas.")
    else:
        print(f"Mokinys su ID {mokinio_id} nerastas.")

def trinti_mokytoja_pagal_id(mokytojo_id):
    mokytojas = session.query(Mokytojas).filter_by(id=mokytojo_id).first()
    if mokytojas:
        session.delete(mokytojas)
        session.commit()
        print(f"Mokytojas su ID {mokytojo_id} buvo istrintas.")
    else:
        print(f"Mokytojas su ID {mokytojo_id} nerastas.")

def trinti_visus_12_klases_mokinius():
    mokiniai = session.query(Mokinys).filter_by(klase=12).all()
    for mokinys in mokiniai:
        session.delete(mokinys)
    session.commit()
    print(f"Visi 12 klasiu mokiniai buvo istrinti.")

def rasti_mokini_pagal_varda():
    mokiniai = session.query(Mokinys).filter_by(vardas='Barbora').all()
    for mokinys in mokiniai:
        print(f"{mokinys.vardas} {mokinys.pavarde}, klase: {mokinys.klase}")
def rasti_mokinius_pagal_pavardes_pradzia():
    mokiniai = session.query(Mokinys).filter(Mokinys.pavarde.ilike('P%')).all()
    for mokinys in mokiniai:
        print(f"{mokinys.vardas} {mokinys.pavarde}, klase: {mokinys.klase}")

def rasti_mokytojus_pagal_vardo_pabaiga():
    mokytojai = session.query(Mokytojas).filter(Mokytojas.vardas.ilike('%s')).all()
    for mokytojas in mokytojai:
        print(f"{mokytojas.vardas} {mokytojas.pavarde}, desto: {mokytojas.dalykas}")


# trinti_mokini_pagal_id(1)

# trinti_mokytoja_pagal_id(2)

# trinti_visus_12_klases_mokinius()

rasti_mokini_pagal_varda()

rasti_mokinius_pagal_pavardes_pradzia()

rasti_mokytojus_pagal_vardo_pabaiga()

# Testuojame funkcijas
# print("Mokiniai:")
# spausdinti_mokinius()
#
# print("\nMokytojai:")
# spausdinti_mokytojus()