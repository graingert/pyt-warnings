import warnings

import pytest

class MyWarning(Warning):
    pass

def do_warning():
    warnings.warn("bad", MyWarning)

@pytest.mark.xfail(reason="should raise a MyWarning")
def test_1():
    do_warning()

@pytest.mark.filterwarnings("always:bad:" + MyWarning.__module__ + "." + MyWarning.__name__)
def test_2():
    do_warning()

@pytest.mark.xfail(reason="should raise a MyWarning")
def test_3():
    do_warning()
