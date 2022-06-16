import av
from typing import Any


class RTSPCapture:
    def __init__(self, rtsp_path: str, rtsp_transport: str = 'tcp', other_options: dict = {}):
        self.__rtsp_path = rtsp_path

        if not other_options:
            other_options = {
                'rtsp_transport': rtsp_transport,
                'fflags': 'nobuffer',
                'flags': 'low_delay',
                'strict': 'experimental'}
        else:
            other_options['rtsp_transport'] = rtsp_transport

        self.__format_ctx = av.open(self.__rtsp_path, 'r', options=other_options)

        self.__stream = self.__format_ctx.streams.video[0]

    def read(self, width: int = None, height: int = None) -> (bool, Any):
        frame = next(self.__format_ctx.decode(self.__stream))
        img = frame.to_ndarray(format='bgr24', interpolation=0x4, width=width, height=height)  # BICUBIC
        return 1, img

    def release(self):
        self.__format_ctx.close()

    @property
    def average_rate(self) -> int:
        return self.__stream.average_rate

    def __del__(self):
        self.release()
