# Александр Швейнов, 10-й поток — Финальный проект. Инженер по тестированию плюс
import new_order
import data

def create_order():
    new_body = data.order.copy()
    track_number = new_order.create_order(new_body)
    return str(track_number.json()["track_number"])
def positive_assert():
    track_num = create_order()
    new_params = data.track_number.copy()
    new_params["t"] = track_num
    response = new_order.get_order(new_params)
    assert response.status_code == 200

def test_order():
    positive_assert()