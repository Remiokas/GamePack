import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine, Date
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///game_stats.db')
Base = declarative_base()

class Score(Base):
    __tablename__ = 'Game Stats'
    id = Column(Integer, primary_key=True)
    game = Column('Game', String)
    play_date = Column('Date', String)
    score = Column('Score', String)


    def __init__(self, game, play_date, score):
        self.game = game
        self.play_date = play_date
        self.score = score

    def __repr__(self):
        return f'{self.id} {self.game} {self.play_date} {self.score}'

Base.metadata.create_all(engine)