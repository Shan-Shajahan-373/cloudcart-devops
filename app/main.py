from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="CloudCart API")

# Temporary in-memory database
products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 60000
    },
    {
        "id": 2,
        "name": "Mouse",
        "price": 800
    }
]


# Product Model
class Product(BaseModel):
    id: int
    name: str
    price: float


# Home Endpoint
@app.get("/")
def home():
    return {
        "application": "CloudCart API",
        "version": "1.0.0",
        "status": "Running"
    }


# Health Check
@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }


# Version Endpoint
@app.get("/version")
def version():
    return {
        "version": "1.0.0"
    }


# Get All Products
@app.get("/products")
def get_products():
    return products


# Get Product By ID
@app.get("/products/{id}")
def get_product(id: int):

    for product in products:
        if product["id"] == id:
            return product

    return {
        "message": "Product not found"
    }


# Add Product
@app.post("/products")
def add_product(product: Product):

    products.append(product.dict())

    return {
        "message": "Product added successfully",
        "product": product
    }


# Delete Product
@app.delete("/products/{id}")
def delete_product(id: int):

    for product in products:

        if product["id"] == id:
            products.remove(product)

            return {
                "message": "Product deleted successfully"
            }

    return {
        "message": "Product not found"
    }