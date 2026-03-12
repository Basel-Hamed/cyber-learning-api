from fastapi import UploadFile


async def analyze_image(file: UploadFile):

    content = await file.read()

    size = len(content)

    return f"Image received successfully. Size: {size} bytes."
