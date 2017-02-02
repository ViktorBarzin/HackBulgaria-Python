import requests
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Mentor, Team, Skill


MENTOR_API = 'https://hackbulgaria.com/hackfmi/api/mentors/'
TEAM_API = 'https://hackbulgaria.com/hackfmi/api/public-teams/'
SKILL_API = 'https://hackbulgaria.com/hackfmi/api/skills/'


def parse_mentors(mentors_json):
    mentor_objs = []
    for mentor in mentors_json:
        pass


def parse_skills(skills_json):
    skill_objs = []
    for skill in skills_json:
        # import ipdb; ipdb.set_trace()# BREAKPOINT)
        skill_objs.append(Skill(id=skill['id'], name=skill['name']))

    return skill_objs


def parse_teams(teams_json):
    team_objs = []
    for team in teams_json:
        new_team = Team(id=team['id'], name=team['name'],
            idea_description=team['idea_description'], repository=team['repository'],
            need_more_members=team['need_more_members'], room=team['room'],
            place=team['place'])
        if team['technologies_full']:
            for skill in team['technologies_full']:
                if skill in new_team.technologies:
                    continue
                new_team.technologies.append(Skill(id=skill['id'], name=skill['name']))
        team_objs.append(new_team)
    # import ipdb; ipdb.set_trace()# BREAKPOINT)

    return team_objs


def main():
    # Setup db engine and initiate session
    engine = create_engine('sqlite:///hackfmi.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # skills_json = requests.get(SKILL_API).json()
    # skill_objs = parse_skills(skills_json)

    teams_json = requests.get(TEAM_API).json()
    team_objs = parse_teams(teams_json)
    # Add models to db

    # session.add_all(skill_objs)
    session.add_all(team_objs)
    session.commit()

    # mentors = requests.get(MENTOR_API).json()
    # import ipdb; ipdb.set_trace()# BREAKPOINT)
    # session.add_all(mentors)



if __name__ == "__main__":
    main()
