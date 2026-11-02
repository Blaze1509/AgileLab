import pytest
from app import calculate_attendance


@pytest.mark.parametrize("attended, total, expected", [
    (10, 10, 100),   # full attendance
    (7, 10, 70),     # partial attendance
    (1, 3, 33.33),   # partial attendance (decimal)
    (0, 0, 0),       # zero classes
    (0, 10, 0),      # attended none
])
def test_valid_attendance(attended, total, expected):
    assert calculate_attendance(attended, total) == expected


@pytest.mark.parametrize("attended, total", [
    (-1, 10),   # negative attended
    (5, -10),   # negative total
    (12, 10),   # attended more than total
])
def test_invalid_values(attended, total):
    with pytest.raises(ValueError):
        calculate_attendance(attended, total)
