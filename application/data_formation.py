import re


def data_consolidation(phonebook):
    for data in phonebook:
        last_name = data[1]
        for check_data in phonebook:
            check_last_name = check_data[1]
            if last_name == check_last_name:
                if data[0] == '':
                    data[0] = check_data[0]
                if data[2] == '':
                    data[2] = check_data[2]
                if data[3] == '':
                    data[3] = check_data[3]
                if data[4] == '':
                    data[4] = check_data[4]
                if data[5] == '':
                    data[5] = check_data[5]
                if data[6] == '':
                    data[6] = check_data[6]
    joint_phonebook = []
    for new_data in phonebook:
        if new_data not in joint_phonebook:
            joint_phonebook.append(new_data)
    return joint_phonebook


def phonebook_formation(contacts_list, pattern_phone, sub_phone):
    phonebook = []
    for person in contacts_list:
        full_name = ' '.join(person[:3]).split(' ')
        data = [full_name[0], full_name[1], full_name[2], person[3],
                person[4], re.sub(pattern_phone, sub_phone, person[5]),
                person[6]]
        phonebook.append(data)
    return data_consolidation(phonebook)



