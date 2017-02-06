from manage_hospital import *


def main():
    hospital = ManageHospital('hospital.db')
    entities = {'patient': 'patients',
                'doctor': 'doctors',
                'hospital': 'hospital_stay'}

    command = input('Enter a command:')
    while command != 'quit' and command != 'exit':
        # check if list command
        if 'list' in command:
            try:
                entity = command.split(' ')[1]
                hospital.list_all(entity.lower())
            except Exception as e:
                print('Command format is: list <entities>')
        # check if add command
        if 'add' in command:
            # check entity type
            try:
                entity = entities[command.split(' ')[1]].lower()
                if entity == 'patients':
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

        if 'delete' in command:
            hospital.delete_entity()

        if 'update' in command:
            # todo: update without the ifs
            entity = input('Enter what do you want to update:')
            if entity == 'patient':
                hospital.update_patient()
            elif entity == 'doctor':
                hospital.update_doctor()
            elif entity == 'hospital stay' or entity == 'hospital_stay':
                hospital.update_hospital_stay()
            else:
                print('ERROR: There is no such object.')
        command = input('Enter another command:')
        print(command)

if __name__ == '__main__':
    main()
