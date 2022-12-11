import html_view
import csv_view
import user_interface
import xml_view


def create_html():
    data = user_interface.get_data()
    html_view.create(data)
    return None


def create_csv():
    data = user_interface.get_data()
    csv_view.create(data)
    return None


def create_xml():
    data = user_interface.get_data()
    xml_view.create(data)
    return None


def from_xml_to_html(filename):
    data = user_interface.get_data_from_xml(filename)
    html_view.create(data, filename)
    return None
