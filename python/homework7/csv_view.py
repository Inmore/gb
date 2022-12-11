def create(data):
    csv = ''
    for i in data:
        csv += '{};'.format(i['id'])
        csv += '{};'.format(i['last_name'])
        csv += '{};'.format(i['name'])
        csv += '{};'.format(i['b_date'])
        csv += '{};'.format(i['job'])
        csv += '{}\n'.format(i['phone'])

    with open('phonebook.csv', 'w') as file:
        file.write(csv)
