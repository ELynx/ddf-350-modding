echo Searching for transmitter

for /f "tokens=2 delims==" %%a in ('wmic LogicalDisk where "VolumeName='DUMBORC'" get DeviceID /value') do (
 set DriveU=%%a
)

echo Found transmitter on %DriveU%, deleting System Volume Information

del /Q %DriveU%"\System Volume Information"
rd %DriveU%"\System Volume Information"

echo Trash deleted

timeout /T 10 
