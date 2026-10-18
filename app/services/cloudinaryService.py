from app.config import settings # Configures Cloudinary on import
from cloudinary import uploader
from uuid import uuid4


def upload_product_image(file_object, product_id: str | None = None):
    unique_id = uuid4().hex

    public_id = (
        f"product_{product_id}_{unique_id}"
        if product_id is not None
        else f"product_{unique_id}"
    )

    result = uploader.upload(
        file_object,
        folder="furnova/products",
        public_id=public_id,
        resource_type="image",
        allowed_formats=["jpg", "jpeg", "png", "webp"],
        overwrite=False,
    )

    return {
        "image_url": result["secure_url"],
        "public_id": result["public_id"],
        "asset_id": result["asset_id"],
    }


def delete_product_image(public_id: str):
    return uploader.destroy(
        public_id,
        invalidate=True,
        resource_type="image",
    )