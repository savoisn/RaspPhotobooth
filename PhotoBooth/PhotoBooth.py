from picamera import PiCamera
from time import sleep
import hug, io

camera=None

@hug.get(output=hug.output_format.image('jpg'))
@hug.cli()
def take_picture(message, message_size:hug.types.number, rotation:hug.types.number, show_preview=False):
    global camera

    if camera == None:
        camera=PiCamera()

    camera.rotation = rotation


    if show_preview:
        self.camera.start_preview()

    camera.annotate_text = message
    camera.annotate_text_size = message_size

    if show_preview:
        sleep(5)
        self.camera.stop_preview()
    stream = io.BytesIO()

    camera.capture(stream, 'jpeg')
    stream.seek(0)
    return stream

@hug.get(output=hug.output_format.image('jpg'))
@hug.cli()
def take_picture_and_send_email(email, message, message_size:hug.types.number, rotation:hug.types.number, show_preview=False):
    global camera

    if camera == None:
        camera=PiCamera()

    camera.rotation = rotation


    if show_preview:
        self.camera.start_preview()

    camera.annotate_text = message
    camera.annotate_text_size = message_size

    if show_preview:
        sleep(5)
        self.camera.stop_preview()
    camera.capture('/home/pi/Desktop/image.jpg')
    return '/home/pi/Desktop/image.jpg'

if __name__ == '__main__':
    take_picture.interface.cli()

