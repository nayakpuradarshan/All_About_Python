import pytest
import dev

def test_tc1():
    actual_data = dev.add_employee("Harshil", 7000, 29)

    assert actual_data == {'name': 'Harshil', 'salary': 7000, 'age': 29}

def test_tc2():
    with pytest.raises(TypeError):
        dev.add_employee("Harshil", -10, 29)

def test_tc3():
    with pytest.raises(ValueError):
        dev.add_employee("Harshil", 7000, -10)

def test_tc4():
    with pytest.raises(ValueError):
        dev.add_employee("Harshil", 7000, 150)
