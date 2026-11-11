from sqlalchemy import Column, Integer, String, create_engine, DateTime, func, Numeric, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.db.postgresDB import Base

# AUTHENTICATION MODULE (Admin Only)
class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, index=True, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


# IMAGE & FILE STORAGE MODULE (Cloudinary-optimized)
class FileStorage(Base):
    __tablename__ = 'file_storage'

    file_id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String(255), nullable=False)        # Original file name
    public_id = Column(String(255), nullable=False, unique=True, index=True) # Cloudinary Public ID (vital for deletions/updates)
    secure_url = Column(String(500), nullable=False)     # HTTPS URL returned by Cloudinary for frontend delivery
    resource_type = Column(String(50), default="image")  # "image", "video", or "raw"
    format = Column(String(50), nullable=True)           # File extension (e.g., "png", "jpg")
    created_at = Column(DateTime(timezone=True), server_default=func.now())


# PRODUCT MODULE
class Product(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    description = Column(String(500), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    stock = Column(Integer, nullable=False, default=0)
    category = Column(String(100), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Foreign Key pointing to FileStorage
    file_id = Column(Integer, ForeignKey('file_storage.file_id', ondelete='SET NULL'), nullable=True)
    created_by = Column(Integer, ForeignKey('user.user_id', ondelete='CASCADE'), nullable=True)

    creator = relationship("User")
    image = relationship("FileStorage")


# CART MODULE
class Cart(Base):
    __tablename__ = 'carts'

    cart_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(String(100), unique=True, nullable=False, index=True)  # Frontend generated UUID/token
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    items = relationship("CartItem", back_populates="cart", cascade="all, delete-orphan")


class CartItem(Base):
    __tablename__ = 'cart_items'

    cart_item_id = Column(Integer, primary_key=True, index=True)
    cart_id = Column(Integer, ForeignKey('carts.cart_id', ondelete='CASCADE'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.product_id', ondelete='CASCADE'), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    price = Column(Numeric(10, 2), nullable=False)

    cart = relationship("Cart", back_populates="items")
    product = relationship("Product")


# CHECKOUT & ORDER MODULES (COD Only)
class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True, index=True)

    # Customer Details
    customer_name = Column(String(150), nullable=False)
    phone = Column(String(20), nullable=False)
    email = Column(String(150), nullable=False)

    address_line1 = Column(String(255), nullable=False)
    address_line2 = Column(String(255), nullable=True)
    district = Column(String(100), nullable=False)
    postal_code = Column(String(20), nullable=False)
    notes = Column(String(500), nullable=True)

    total_amount = Column(Numeric(10, 2), nullable=False)
    status = Column(String(50), default="Pending")  # Pending, Confirmed, Preparing, Ready, Delivered, Cancelled

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")


class OrderItem(Base):
    __tablename__ = 'order_items'

    order_item_id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey('orders.order_id', ondelete='CASCADE'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.product_id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)

    order = relationship("Order", back_populates="items")
    product = relationship("Product")