from parking import calculate_usage_score, get_utilization_status


def test_usage_score():
    assert calculate_usage_score(10, 5) == 50
    assert calculate_usage_score(15, 6) == 90


def test_over_utilized():
    assert get_utilization_status(95) == "Over-Utilized Parking Area"


def test_optimally_utilized():
    assert get_utilization_status(70) == "Optimally Utilized Parking Area"


def test_under_utilized():
    assert get_utilization_status(30) == "Under-Utilized Parking Area"
