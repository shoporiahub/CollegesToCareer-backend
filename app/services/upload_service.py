from fastapi import HTTPException, UploadFile, status

import cloudinary.uploader

import app.core.cloudinary  # noqa: F401


ALLOWED_IMAGE_TYPES = {
    "image/jpeg",
    "image/png",
    "image/webp",
}

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB


async def upload_profile_photo(
    file: UploadFile,
) -> str:
    """
    Upload a profile photo to Cloudinary
    and return its secure URL.
    """

    if file.content_type not in ALLOWED_IMAGE_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                "Invalid image type. "
                "Only JPEG, PNG, and WebP images are allowed."
            ),
        )

    contents = await file.read()

    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Profile photo must be smaller than 5 MB.",
        )

    try:
        result = cloudinary.uploader.upload(
            contents,
            folder="resume-ai/profile-photos",
            resource_type="image",
        )

        return result["secure_url"]

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Image upload failed.",
        )