from euchre.rank import Rank


def test_names():
    _r = Rank()
    assert sorted(list(_r.names.keys())) == sorted(
        ["7", "8", "9", "10", "J", "Q", "K", "A"]
    )


def test_natural_ranks():
    _r = Rank()
    assert sorted(list(_r.natural_ranks)) == sorted(
        ["Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
    )


def test_non_bowers():
    _r = Rank()
    assert "J" not in _r.non_bowers
    assert sorted(["7", "8", "9", "10", "Q", "K", "A"]) == sorted(list(_r.non_bowers))
