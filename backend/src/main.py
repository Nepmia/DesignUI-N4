from .entities.entity import Session, engine, Base
from .entities.dbtest import Test

Base.metadata.create_all(engine)

session = Session()

tests = session.query(Test).all()

if len(tests) == 0:
    testing = Test("DSUI DB TEST", "connection to db is ok")
    session.add(testing)
    session.commit()
    session.close()

    tests = session.query(Test).all()

print('Tests:')
for test in tests:
    print(f'({test.id}) {test.title} - {test.description}')