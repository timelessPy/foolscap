import os
import pickle


from file_paths import NOTE_DATA


# Write example data:
def save_data(data):
    """:param data: (dict) containing all notes."""
    with open(NOTE_DATA, 'wb') as output:
        pickle.dump(data, output, pickle.HIGHEST_PROTOCOL)


def note_data():
    """ Load the note data into a dict."""
    try:
        with open(NOTE_DATA, 'rb') as _input:
            return pickle.load(_input)

    except EOFError and IOError:
        return {}

