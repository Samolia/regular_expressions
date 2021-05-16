import csv


def get_contacts_list(file_name):
    with open(file_name, encoding='utf-8') as file:
        rows = csv.reader(file, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


def save_data(phonebook):
    with open("result_data/phonebook.csv", "w", encoding='utf-8', newline='') as file:
        data_writer = csv.writer(file, delimiter=',')
        data_writer.writerows(phonebook)
        return 'Информация успешно записана! Проверьте "result_data/phonebook.csv"'
