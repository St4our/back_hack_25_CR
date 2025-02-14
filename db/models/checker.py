import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Импортируем все модели
from db.base_model import Model
from db.models.fighters import Fighter
from db.models.awards import Award
from db.models.events import Event
from db.models.municipalities import Municipality
from db.models.users import User
from db.models.fighter_award_association import fighter_award_association
from db.models.fighter_event_association import fighter_event_association

# Создаём подключение к SQLite
DATABASE_URL = "sqlite:///test_database.db"
engine = create_engine(DATABASE_URL, echo=True)

# Создаём таблицы в базе данных
Model.metadata.create_all(engine)

# Создаём сессию
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# --- Добавляем тестовые данные ---

# Создаём муниципалитет
municipality = Municipality(title="Город-герой")
session.add(municipality)
session.commit()

# Создаём бойца
fighter = Fighter(
    name="Иван Иванов",
    birth_death_years="1920-1945",
    municipality_id=municipality.id,
    short_info="Герой войны",
    photo_path="ivan_ivanov.jpg"
)
session.add(fighter)
session.commit()

# Создаём награду
award = Award(
    name="Орден Славы",
    photo_path="orden_slavy.jpg",
    description="Высшая награда за отвагу"
)
session.add(award)
session.commit()

# Создаём событие
event = Event(
    title="Битва за Москву",
    info="Оборона Москвы в 1941 году"
)
session.add(event)
session.commit()

# Связываем бойца с наградой и событием
fighter.awards.append(award)
fighter.events.append(event)
session.commit()

# --- Проверяем логику ---

# 1. Проверяем бойца и его связи
fighter_from_db = session.query(Fighter).filter_by(name="Иван Иванов").first()
print(f"Боец: {fighter_from_db.name}, Муниципалитет: {fighter_from_db.municipality.title}")

# 2. Проверяем его награды
for award in fighter_from_db.awards:
    print(f"Награда: {award.name}, Описание: {award.description}")

# 3. Проверяем его участие в событиях
for event in fighter_from_db.events:
    print(f"Событие: {event.title}, Описание: {event.info}")

# Закрываем сессию
session.close()
