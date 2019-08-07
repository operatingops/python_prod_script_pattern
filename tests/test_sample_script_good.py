from unittest import mock

from sample_scripts import good


def test_offset_under_threshold_is_actionable():
    assert good.offset_is_actionable(offset=4)


def test_offset_over_threshold_is_not_actionable():
    assert not good.offset_is_actionable(offset=6)


def test_offset_under_threshold_runs():
    with mock.patch.object(good, 'act_on_offset') as p:
        good.run(offset=4, simulate=True)
    assert p.called


def test_offset_over_threshold_does_not_run():
    with mock.patch.object(good, 'act_on_offset') as p:
        good.run(offset=6, simulate=True)
    assert not p.called


def test_done_when_simulate_false():
    with mock.patch('time.sleep'):
        assert good.act_on_offset(1, simulate=False)


def test_not_done_when_simulate_true():
    assert not good.act_on_offset(1, simulate=True)


def test_sleeps_when_simulate_false():
    """
    In a real script this would do something like test that the right API call
    was made.
    """
    with mock.patch('time.sleep') as p:
        good.act_on_offset(1, simulate=False)
        assert p.called


def test_does_not_sleep_when_simulate_true():
    """
    In a real script this would do something like test that _no_ API calls
    were made.
    """
    with mock.patch('time.sleep') as p:
        good.act_on_offset(1, simulate=True)
        assert not p.called
