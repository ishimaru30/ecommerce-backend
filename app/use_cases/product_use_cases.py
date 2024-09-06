from app.repository.product_repository import ProductRepository
from app.domain.entities.product import Product

class ProductUseCase:
    def __init__(self, product_repo: ProductRepository):
        self.product_repo = product_repo

    def add_product(self, name, description, price, stock):
        product = Product(name=name, description=description, price=price, stock=stock)
        self.product_repo.add_product(product)

    def get_products(self):
        return self.product_repo.get_all_products()
