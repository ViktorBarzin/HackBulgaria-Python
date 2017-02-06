from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


mentorship_table = Table('mentorship', Base.metadata,
                        Column('mentor_id', ForeignKey('mentor.id')),
                        Column('team_id', ForeignKey('team.id')))

technology_team = Table('teamskill', Base.metadata,
                        Column('team_id', ForeignKey('team.id')),
                        Column('technology_id', ForeignKey('skill.id')))


class Team(Base):
    __tablename__ = 'team'

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    idea_description = Column(String(500))
    repository = Column(String(500))
    need_more_members = Column(Boolean)
    members_needed_desc = Column(String(250))
    room = Column(String(250))
    place = Column(Integer, default=None)

    skill = relationship('Skill', back_populates='team', secondary=technology_team)
    # team_skill_id = Column(Integer, ForeignKey('teamskill.team_id'))
    mentor = relationship('Mentor', back_populates='team', secondary=mentorship_table)


class Mentor(Base):
    __tablename__ = 'mentor'

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    description = Column(String(500))
    picture = Column(String(250))
    # team_id = Column(Integer, ForeignKey('team.id'))

    team = relationship('Team', secondary=mentorship_table,
                        back_populates='mentor')


class Skill(Base):
    __tablename__ = 'skill'

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    team = relationship('Team', secondary=technology_team, back_populates='skill')



if __name__ == '__main__':
    engine = create_engine('sqlite:///hackfmi.db')
    # Session = sessionmaker(bind=engine)
    # session = Session()
    Base.metadata.create_all(engine)
