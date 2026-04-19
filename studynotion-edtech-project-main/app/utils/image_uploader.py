from fastapi import UploadFile
import cloudinary
import cloudinary.uploader

from app.core.config import settings


def configure_cloudinary() -> None:
    if not (settings.cloud_name and settings.cloud_api_key and settings.cloud_api_secret):
        raise RuntimeError("Cloudinary settings are not configured")
    cloudinary.config(
        cloud_name=settings.cloud_name,
        api_key=settings.cloud_api_key,
        api_secret=settings.cloud_api_secret,
    )


def upload_image_to_cloudinary(file: UploadFile, folder: str | None, height: int | None = None, quality: int | None = None):
    configure_cloudinary()
    options: dict = {"resource_type": "auto"}
    if folder:
        options["folder"] = folder
    if height:
        options["height"] = height
    if quality:
        options["quality"] = quality

    return cloudinary.uploader.upload(file.file, **options)
