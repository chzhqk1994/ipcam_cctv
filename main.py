import cv2
import datetime

SHOW_STREAM = True
VIDEO_SOURCE = 1


class StreamRecorder:
    def __init__(self, save_dir):
        self.save_dir = save_dir
        self.cap = cv2.VideoCapture(VIDEO_SOURCE)

        # Get the Default resolutions
        self.frame_width = int(self.cap.get(3))
        self.frame_height = int(self.cap.get(4))

        filename = str(datetime.datetime.now()).split('.')[0].replace(":", "_") + '.avi'

        # Define the codec and filename.
        self.out = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 30, (self.frame_width, self.frame_height))

    def closeSession(self):
        self.cap.release()
        self.out.release()
        cv2.destroyAllWindows()

    def run_program(self):
        while True:
            try:
                if self.cap.isOpened():
                    ret, image = self.cap.read()
                    if ret:
                        self.out.write(image)

                    # show video stream
                    if SHOW_STREAM:
                        cv2.imshow('stream', image)
                        if cv2.waitKey(5) & 0xFF == ord('q'):
                            self.closeSession()
                            break

                else:
                    self.cap.release()
                    self.cap = cv2.VideoCapture(VIDEO_SOURCE)
            except cv2.error as e:
                print(e)
                self.cap.release()
                self.cap = cv2.VideoCapture(VIDEO_SOURCE)


if __name__ == '__main__':
    obj = StreamRecorder(save_dir='./')
    obj.run_program()
