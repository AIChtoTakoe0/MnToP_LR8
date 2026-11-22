"""ЛР8, задание 5: TDD — реализация API, написанная ПОСЛЕ тестов (шаг Green).

Тесты в test_main.py уже определили контракт: коды 201/200/404/422,
поля id/name/price, запрет price <= 0 и пустого name.
Запуск сервера: uvicorn main:app --reload  (документация Swagger: /docs)
"""
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

# Модель входных данных: ограничения полей дают код 422 при нарушении
class ProductIn(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(gt=0)

# Ответ: входные поля плюс сгенерированный id
class Product(ProductIn):
    id: int

app = FastAPI(title="ЛР8 задание 5 — API «Товары» (TDD)")

# Хранилище в памяти (после перезапуска данные исчезают — для лабораторной достаточно)
_products: dict[int, Product] = {}
_next_id = 1


@app.post("/products", response_model=Product,
          status_code=status.HTTP_201_CREATED)
def create_product(data: ProductIn) -> Product:
    global _next_id
    product = Product(id=_next_id, **data.model_dump())
    _products[product.id] = product
    _next_id += 1
    return product


@app.get("/products", response_model=list[Product])
def list_products() -> list[Product]:
    return list(_products.values())


@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int) -> Product:
    if product_id not in _products:
        raise HTTPException(status_code=404, detail="Товар не найден")
    return _products[product_id]
