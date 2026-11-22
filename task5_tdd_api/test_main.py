"""ЛР8, задание 5: TDD — этот файл написан ДО реализации (шаг Red).

Тесты описывают ожидаемое поведение REST API «Товары»:
POST /products   -> 201 и созданный объект
GET  /products   -> 200 и список
GET  /products/1 -> 200 и объект по id
GET  /products/999 -> 404
POST с price <= 0 или пустым name -> 422 (валидация Pydantic)

Запуск: cd task5_tdd_api && python -m pytest -v
"""
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_create_product_returns_201_and_body():
    resp = client.post("/products", json={"name": "Чай", "price": 199.9})
    assert resp.status_code == 201
    body = resp.json()
    assert body["id"] == 1
    assert body["name"] == "Чай"
    assert body["price"] == 199.9


def test_get_products_list():
    client.post("/products", json={"name": "Кофе", "price": 349.0})
    resp = client.get("/products")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)
    assert any(p["name"] == "Кофе" for p in resp.json())


def test_get_product_by_id():
    resp = client.get("/products/1")
    assert resp.status_code == 200
    assert resp.json()["id"] == 1


def test_get_missing_product_returns_404():
    resp = client.get("/products/999")
    assert resp.status_code == 404


def test_negative_price_rejected_422():
    resp = client.post("/products", json={"name": "Гвоздь", "price": -1})
    assert resp.status_code == 422


def test_empty_name_rejected_422():
    resp = client.post("/products", json={"name": "", "price": 5})
    assert resp.status_code == 422
