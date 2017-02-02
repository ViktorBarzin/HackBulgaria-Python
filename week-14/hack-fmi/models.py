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

    technologies = relationship('Skill', secondary=technology_team)
    # team_skill_id = Column(Integer, ForeignKey('teamskill.team_id'))
    # mentors = relationship('mentor', backref='teams', secondary='mentorship')

# class Mentorship(Base):
#     __tablename__ = 'mentorship'

#     id = Column(Integer, primary_key=True)
#     mentor_id = Column(Integer, ForeignKey('mentor.id'))
#     team_id = Column(Integer, ForeignKey('team.id'))


class Mentor(Base):
    __tablename__ = 'mentor'

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    description = Column(String(500))
    picture = Column(String(250))
    # team_id = Column(Integer, ForeignKey('team.id'))

    teams = relationship('Team', backref='mentors', secondary=mentorship_table)



# class TeamSkill(Base):
#     __tablename__ = 'teamskill'

#     id = Column(Integer, primary_key=True)
#     team_id = Column(Integer, ForeignKey('team.id'))
#     skill_id = Column(Integer, ForeignKey('skill.id'))


class Skill(Base):
    __tablename__ = 'skill'

    id = Column(Integer, primary_key=True)
    name = Column(String(250))


if __name__ == '__main__':
    engine = create_engine('sqlite:///hackfmi.db')
    # Session = sessionmaker(bind=engine)
    # session = Session()
    Base.metadata.create_all(engine)
