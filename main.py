from application import get_contacts_list, save_data, phonebook_formation


if __name__ == '__main__':
    pattern_phone = r'(\+7|8)\s?\(?(\d{3})\)?[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d+)\s?(\(?(доб\.)\s?(\d{4})\)?)?'
    sub_phone = r'+7(\2)\3-\4-\5 \7\8'
    print(save_data(phonebook_formation(get_contacts_list('data/phonebook_raw.csv'), pattern_phone, sub_phone)))
