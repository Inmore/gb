def create(data):
    xml = '<?xml version="1.0" encoding="windows-1251"?>\n'
    xml += '<phonebook>\n'
    for i in data:
        xml += '<user>\n'
        xml += f"    <id>{i['id']}</id>\n"
        xml += f"    <last_name>{i['last_name']}</last_name>\n"
        xml += f"    <name>{i['name']}</name>\n"
        xml += f"    <b_date>{i['b_date']}</b_date>\n"
        xml += f"    <job>{i['job']}</job>\n"
        xml += f"    <phone>{i['phone']}</phone>\n"
        xml += '</user>\n'
    xml += '</phonebook>\n'

    with open('phonebook.xml', 'w') as file:
        file.write(xml)
