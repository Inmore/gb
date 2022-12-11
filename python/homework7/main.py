import controller


if __name__ == '__main__':
    controller.create_xml()
    controller.create_html()
    controller.create_csv()
    controller.from_xml_to_html('phonebook.xml')
