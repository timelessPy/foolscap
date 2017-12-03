from mock import call
from mock import patch
from mock import MagicMock

from foolscap.cli import main


# foolscap.cli.note_data
FAKE_DATA = 'mock_data'


def make_test_args(tup):
    sample_args = ['foolscap/cli.py']
    sample_args.extend(tup)
    return sample_args


def test_valid_command():
    test_args = make_test_args(['save', 'mock_note.txt'])
    with patch('sys.argv', test_args),\
         patch('foolscap.cli.load_data', side_effect=[FAKE_DATA]),\
         patch('foolscap.cli.action') as mock_action:

        expected = call('save', FAKE_DATA, 'mock_note.txt')
        main()
        assert mock_action.call_args == expected


def test_valid_command_optional():
    """ Test optional arg
    """
    test_args = make_test_args(['new'])
    with patch('sys.argv', test_args),\
         patch('foolscap.cli.load_data', side_effect=[FAKE_DATA]),\
         patch('foolscap.cli.action') as mock_action:

        expected = call('new', FAKE_DATA, None)
        main()
        assert mock_action.call_args == expected


def test_invalid_command():
    # Must do:
    pass