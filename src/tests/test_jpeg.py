import logging
from io import BytesIO

from PIL import Image

logger = logging.getLogger(__name__)


def test_write_jpeg():
    """See if Pillow can write JPEG (tests linkage against mozjpeg)"""
    im = Image.new('RGB', (10, 10))
    buffer = BytesIO()
    im.save(buffer, format='JPEG')

    size = buffer.getbuffer().nbytes
    if size != 375:
        logger.error("JPEG optimization is not working as expected! size=%s", size)
