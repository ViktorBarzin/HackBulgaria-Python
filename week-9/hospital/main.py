from manage_hospital import *

hospital = ManageHospital('hospital.db')
commands = {'add patient': hospital.add_patient,
            'add doctor': hospital.add_doctor,
            'add hospital stay': hospital.add_hospital_stay,
            'update patient': hospital.update_patient,
            'update doctor': hospital.update_doctor,
            'update hospital stay': hospital.update_hospital_stay,
            'delete patient': hospital.delete_entity,
            'delete doctor': hospital.delete_entity,
            'delete hospital stay': hospital.delete_entity}
entities = {'patients': 'patients',
            'doctors': 'doctors',
            'hospital': 'hospital_stay'}


command = input('Enter a command:')
while command != 'quit' and command != 'exit':
    # check if list command
    if 'list' in command:
        # try:
        entity = command.split(' ')[1]
        hospital.list_all(entity.lower())
        # except Exception as e:
        #     print('Invalid list command')
        #     print(e)
    # check if add command
    if 'add' in command:
        # check entity type
        try:
            entity = entities[command.split(' ')[1]].lower()
            if entity == 'patients' or entity == 'patient':
                # add patient
                hospital.add_patient()
            elif entity == 'doctors' or entity == 'doctor':
                # add doctor
                hospital.add_doctor()
            elif entity == 'hospital_stay':
                # add hospital stay
                hospital.add_hospital_stay()
        except:
            print('Invalid add command')

    command = input('Enter another command:')
    print(command)


