from picamera import PiCamera
from time import sleep
import hug, io
import SendEmail

camera=None

@hug.get(output=hug.output_format.image('png'))
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

    camera.capture(stream, 'png')
    stream.seek(0)
    return stream

@hug.get(output=hug.output_format.image('png'))
@hug.cli()
def take_picture_and_send_email(email_adress, message, message_size:hug.types.number, rotation:hug.types.number, show_preview=False):
    stream = take_picture(message, message_size, rotation, show_preview)
    SendEmail.sendMail(stream, email_adress)
    stream.seek(0)
    return stream



if __name__ == '__main__':
    take_picture_and_send_email.interface.cli()
    # take_picture.interface.cli()

