from models import db, Pet
from app import app

db.drop_all()
db.create_all()


p1 = Pet(name="Fluffy", species="cat", age=3, photo_url="https://images.unsplash.com/photo-1573865526739-10659fec78a5?q=80&w=2815&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
p2 = Pet(name="Boo", species="dog", age=1)
p3 = Pet(name="Donut", species="cat", age=7)
p4 = Pet(name="Alpha", species="porcupine", photo_url="https://images.unsplash.com/photo-1570481662006-a3a1374699e8?q=80&w=2274&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
db.session.add_all([p1, p2, p3, p4])
db.session.commit()