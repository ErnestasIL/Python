from sqlalchemy import Column, create_engine, Integer, String, func
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///mokykla2nd.db')
Base = declarative_base()

class Mokinys(Base):
    __tablename__ = 'mokinys'
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)
    klase = Column(Integer)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

mokiniai = [
    Mokinys(vardas="Jonas", pavarde="Jonaitis", klase=5),
    Mokinys(vardas="Petras", pavarde="Petraitis", klase=6),
    Mokinys(vardas="Asta", pavarde="Astaitė", klase=7),
    Mokinys(vardas="Barbora", pavarde="Radvilaite", klase=10),
    Mokinys(vardas="Kastytis", pavarde="Kerbedis", klase=12),
    Mokinys(vardas="Marius", pavarde="Mclarenas", klase=12),
]
# session.add_all(mokiniai)
session.commit()

def spausdinti_mokinius():
    mokiniai = session.query(Mokinys).all()
    for mokinys in mokiniai:
        print(f"{mokinys.id}. {mokinys.vardas} {mokinys.pavarde}, klase: {mokinys.klase}")

def didejancia():
    mokiniai = session.query(Mokinys).order_by(Mokinys.klase).all()
    if mokiniai:
        for mokinys in mokiniai:
            print(f"{mokinys.id}. {mokinys.vardas} {mokinys.pavarde}, klase: {mokinys.klase}")
    else:
        print("Nerasta mokiniu.")

def skaiciuoti_mokinius_kiekvienoje_klaseje():
    results = session.query(Mokinys.klase, func.count(Mokinys.id)).group_by(Mokinys.klase).all()
    for klase, kiekis in results:
        print(f"Klase {klase}: {kiekis} mokiniai")

def vidutinis_mokiniu_skaicius():
    total_students = session.query(func.count(Mokinys.id)).scalar()
    total_classes = session.query(func.count(func.distinct(Mokinys.klase))).scalar()

    if total_classes > 0:
        vidurkis = total_students / total_classes
        print(f"Vidutinis mokiniu skaicius klaseje: {vidurkis:.2f}")
    else:
        print("Nera duomenų apie klases.")

spausdinti_mokinius()
print('-' * 30)
didejancia()
print('-' * 30)
skaiciuoti_mokinius_kiekvienoje_klaseje()
print('-' * 30)
vidutinis_mokiniu_skaicius()