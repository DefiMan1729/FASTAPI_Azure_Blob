from fastapi import FastAPI, HTTPException, UploadFile
from azure.storage.blob.aio import BlobServiceClient
import requests
import ssl
app = FastAPI()

@app.post("/uploadfile")
async def create_upload_file(file: UploadFile):
    name = file.filename
    type = file.content_type
    return await uploadtoazure(file,name,type)

async def uploadtoazure(file: UploadFile,file_name: str,file_type:str):
    connect_str = "<storage account connection string>"
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_name = "<test_container>"
    async with blob_service_client:
            container_client = blob_service_client.get_container_client(container_name)
            try:
                blob_client = container_client.get_blob_client(file_name)
                f = await file.read()
                await blob_client.upload_blob(f)
            except Exception as e:
                print(e)
                return HTTPException(401, "Something went terribly wrong..")
    
    return "{'status':'file uploaded successdully'}"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, )  