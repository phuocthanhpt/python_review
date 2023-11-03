import pytest


@pytest.mark.accumulator
def test_accumulator_add_one(accum):
    # accum = Accumulator()
    accum.add()
    assert accum.get_count == 1


@pytest.mark.accumulator
def test_accumulator_add_three(accum):
    # accum = Accumulator()
    accum.add(3)
    assert accum.get_count == 3


@pytest.mark.accumulator
def test_accumulator_init(accum):
    # accum = Accumulator()
    assert accum.get_count == 0


@pytest.mark.accumulator
def test_accumulator_add_twice(accum):
    # accum = Accumulator()
    accum.add()
    accum.add()
    assert accum.get_count == 21


@pytest.mark.accumulator
def test_accumulator_cannot_set_count_directly(accum):
    # accum = Accumulator()
    with pytest.raises(AttributeError, match=r"property 'get_count' of 'Accumulator' object has no setter") as e:
        accum.get_count = 10
