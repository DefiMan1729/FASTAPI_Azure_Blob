# FastAPI Azure Blob Storage Integration

This repository contains a simple **FastAPI** application that allows users to upload files and store them in an **Azure Blob Storage** container. The app also provides endpoints for handling file uploads and error handling.

## Features

1. **File Upload Endpoint**:
   - Users can upload files using the `/uploadfile` endpoint.
   - The uploaded file is stored in an Azure Blob Storage container.

2. **Azure Blob Storage Integration**:
   - The app connects to an Azure Blob Storage account using the provided connection string and container name

3. **Error Handling**:
   - If any exceptions occur during the file upload process, the app returns an appropriate HTTP error response.

