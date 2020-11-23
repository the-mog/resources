import pytest


@pytest.fixture
def assert_tx_failed():
    def assert_revert(function):
        with pytest.raises(ValueError, message="Transaction did not fail.") as e:
            function()
        assert "VM Exception while processing transaction" in str(e), \
               "Did not find VM exception in error message."
    return assert_revert
