# Main FastAPI application
# --------------------------------------

# Imports
# --------------------------------------
from fastapi import FastAPI
from pydantic import BaseModel
import requests
from datetime import datetime
import xml.etree.ElementTree as ET

from starlette.responses import FileResponse


# --------------------------------------
# Application
# --------------------------------------
class NetworkSpeedLog(BaseModel):
    """Network speed log model"""
    download_speed: float
    timestamp: str

    # Add an XML method to the model
    def xml(self):
        """Return XML"""
        # Create XML
        xml = ET.Element('speedtest')
        xml.set('timestamp', self.timestamp)
        xml.set('download_speed', str(self.download_speed))
        # Return XML
        return xml


app = FastAPI()


# --------------------------------------
# Functions
# --------------------------------------
def check_speed(file_url):
    global speed
    start_time = datetime.now()
    file = requests.get(file_url, stream=True)
    total_length = file.headers.get('content-length')
    if total_length is None:
        return 0
    else:
        dl = 0
        total_length = int(total_length)
        for data in file.iter_content(chunk_size=4096):
            dl += len(data)
            done = int(50 * dl / total_length)
            speed = dl / 1024 / 1024 / (datetime.now() - start_time).total_seconds() * 8
            print(f"\r[{'=' * done}{' ' * (50 - done)}] {speed:.2f} MB/s", end='')


def get_speed():
    # Check speed
    check_speed('http://ipv4.download.thinkbroadband.com/5MB.zip')

    # Return speed
    return {"speed": "{:.2f}".format(speed) + " MB/s"}


def record_speed_log():
    # Check speed
    check_speed('http://ipv4.download.thinkbroadband.com/5MB.zip')

    # Record speed log
    log = NetworkSpeedLog(
        download_speed=speed,
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

    # Create XML file
    xml_file = ET.ElementTree(log.xml())
    xml_file.write("speed_log.xml")

    # Return speed log
    return log


# --------------------------------------
# Routes
# --------------------------------------
@app.get("/speed")
async def speed():
    """Speed route"""

    # Record speed log
    record_speed_log()

    # Download speed file
    return FileResponse("speed_log.xml", media_type="application/xml", filename="speed_log.xml")


@app.get("/speed_log")
async def speed_log():
    """Speed log route"""

    # Get speed log
    return get_speed(), 200
