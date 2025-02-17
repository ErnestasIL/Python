from teorija import Projektas, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

pavadinimas = input('iveskite projekto pavadinima: ')
kaina = float(input('iveskite kaina: '))


row_object = Projektas(pavadinimas=pavadinimas, kaina=kaina)
session.add(row_object)
session.commit()

all_rows = session.query(Projektas).all()

for row in all_rows:
    print(f'ID yra: {row.id}, pavadinimas yra: {row.pavadinimas}, kaina {row.kaina}')