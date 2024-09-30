@echo off
setlocal enabledelayedexpansion

:: Prompt for folder path
set /p folder="Enter the folder path: "

:: Check if folder exists
if not exist "%folder%" (
    echo Folder "%folder%" does not exist.
    exit /b
)

:: Change to the specified folder
pushd "%folder%"

:: Prompt for extensions
set /p extensions="Enter the file extensions to gzip (separated by space, e.g., wasm pck): "

:: Loop through extensions and gzip matching files
for %%e in (%extensions%) do (
    for %%f in (*%%e) do (
        echo Compressing %%f
        gzip -c "%%f" > "%%f.gz"
    )
)

echo All files compressed.

:: Prompt for S3 folder name (optional)
set /p s3folder="Enter the S3 folder name (optional, leave blank for root): "

:: Adjust S3 destination
if "%s3folder%"=="" (
    set s3path=s3://%S3_BUCKET_ROOT%/
) else (
    set s3path=s3://%S3_BUCKET_ROOT%/%s3folder%/
)

:: Upload all files (both compressed and uncompressed) to S3
echo Uploading all files to S3...
for %%f in (*) do (
    echo Uploading %%f
    aws s3 cp "%%f" %s3path%
)

:: Update metadata for .wasm.gz and .pck.gz files in S3
for %%e in (wasm pck) do (
    for %%f in (*%%e.gz) do (
        echo Updating metadata for %%f
        aws s3 cp %s3path%%%f %s3path%%%f --metadata-directive REPLACE --content-encoding gzip
)
)

echo All files uploaded and metadata updated.
pause

:: Return to the original directory
popd
