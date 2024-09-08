from app.repository.product_repository import ProductRepository
from app.domain.entities.product import Product

class ProductUseCase:
    def __init__(self, product_repo):
        self.product_repo = product_repo

    def add_product(self, name, description, price, stock):
        product = Product(name=name, description=description, price=price, stock=stock)
        self.product_repo.add_product(product)

    def update_product(self, product_id, updated_fields):
        self.product_repo.update_product(product_id, updated_fields)

    def delete_product(self, product_id):
        self.product_repo.delete_product(product_id)