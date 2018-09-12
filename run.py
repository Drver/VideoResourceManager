from ui.VideoResourceManagerWidget import VideoResourceManager
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    v = VideoResourceManager()
    v.show()

    sys.exit(app.exec_())
