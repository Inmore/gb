import data_generator


def get_data():
    return data_generator.generate_data()


def get_data_from_xml(filename):
    return data_generator.data_from_xml(filename)
