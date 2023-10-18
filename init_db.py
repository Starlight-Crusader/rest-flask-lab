from app import create_app, db, EScooter


def init_database():
    app = create_app()
    
    with app.app_context():
        db.create_all()

        sample_scooter_1 = EScooter(name='Scooter 1', battery_level=90.5)
        sample_scooter_2 = EScooter(name='Scooter 2', battery_level=80.0)
        db.session.add(sample_scooter_1)
        db.session.add(sample_scooter_2)
        db.session.commit()


if __name__ == '__main__':
    init_database()