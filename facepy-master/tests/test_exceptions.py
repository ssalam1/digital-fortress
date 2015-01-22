"""Tests for the ``exceptions`` module."""
try:
    import cPickle as pickle
except ImportError:
    import pickle


from nose.tools import *

from facepy import *
from facepy.exceptions import FacebookError


def test_facepy_error():
    try:
        raise FacepyError('<message>')
    except FacepyError as exception:
        if hasattr(exception, "message"):
            assert_equal(exception.message, '<message>')
        assert_equal(exception.__str__(), '<message>')
        assert_equal(exception.__repr__(), 'FacepyError(\'<message>\',)')


def test_facebook_error():
    try:
        raise FacebookError('<message>', 100)
    except FacebookError as exception:
        assert_equal(exception.message, '<message>')
        assert_equal(exception.code, 100)
        assert_equal(exception.__str__(), '[100] <message>')
        assert_equal(exception.__repr__(), 'FacebookError(\'[100] <message>\',)')


def test_facebookerror_can_be_pickled():
    try:
        raise GraphAPI.FacebookError('<message>', '<code>')
    except FacepyError as exception:
        pickle.dumps(exception)


def test_oautherror_can_be_pickled():
    try:
        raise GraphAPI.OAuthError('<message>', '<code>')
    except FacepyError as exception:
        pickle.dumps(exception)


def test_httperror_can_be_pickled():
    try:
        raise GraphAPI.HTTPError('<message>')
    except FacepyError as exception:
        pickle.dumps(exception)
