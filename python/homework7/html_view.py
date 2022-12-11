def create(data, filename='index'):
    style = 'style="font-size:14px"'
    html = '<html>\n <head><meta charset="windows-1251"></head>\n   <body>\n'
    for i in data:
        html += '<div style="margin-top: 40px">\n'
        html += '    <p {}><b>id:</b> {}</p>\n'.format(style, i['id'])
        html += '    <p {}><b>Фамилия:</b> {}</p>\n'.format(style, i['last_name'])
        html += '    <p {}><b>Имя:</b> {}</p>\n'.format(style, i['name'])
        html += '    <p {}><b>Дата рождения:</b> {}</p>\n'.format(style, i['b_date'])
        html += '    <p {}><b>Место работы:</b> {}</p>\n'.format(style, i['job'])
        html += '    <p {}><b>Телефон:</b> {}</p>\n'.format(style, i['phone'])
        html += '</div>\n'
    html += '   </body>\n</html>'
    

    with open(f'{filename}.html', 'w') as page:
        page.write(html)
