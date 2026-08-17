from fastapi import APIRouter, File, UploadFile

from app.services.upload_service import upload_profile_photo


router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)


@router.post("/profile-photo")
async def upload_photo(
    file: UploadFile = File(...),
):
    url = await upload_profile_photo(file)

    return {
        "message": "Profile photo uploaded successfully",
        "url": url,
    }