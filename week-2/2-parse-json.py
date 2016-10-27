import json
import sys

JSON_DICT_PEOPLE_ENTRY = 'people'
SKILLS_FIELD = 'skills'
SKILL_NAME_FIELD = 'name'
SKILL_LEVEL_FIELD = 'level'
PERSON_FIRST_NAME_FIELD = 'first_name'
PERSON_LAST_NAME_FIELD = 'last_name'


def parse_json(file_path):
    with open(file_path, 'r') as j:
        return json.load(j)
    pass


def get_languages_from_json_dict(json_dict):
    languages = []

    for person in json_dict[JSON_DICT_PEOPLE_ENTRY]:
        for skill in person[SKILLS_FIELD]:
            languages.append(skill[SKILL_NAME_FIELD])
    return set(languages)


def get_best_from_each_language(json_dict):
    languages = get_languages_from_json_dict(json_dict)
    lang_max_score = {x:0 for x in languages}
    lang_max_score_name = {}

    for person in json_dict[JSON_DICT_PEOPLE_ENTRY]:
        for skill in person[SKILLS_FIELD]:
            skill_name = skill[SKILL_NAME_FIELD]
            if lang_max_score[skill_name] < skill[SKILL_LEVEL_FIELD]:
                lang_max_score[skill_name] = skill[SKILL_LEVEL_FIELD]
                lang_max_score_name[skill_name] = person[PERSON_FIRST_NAME_FIELD] + ' ' + person[PERSON_LAST_NAME_FIELD]
    return '\n'.join([(key + ' - ' + lang_max_score_name[key]) for key in lang_max_score_name.keys()])


def main():
    json_dict = parse_json(sys.argv[1])
    print(get_best_from_each_language(json_dict))
    pass

if __name__ == '__main__':
    main()