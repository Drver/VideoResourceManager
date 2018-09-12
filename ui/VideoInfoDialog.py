from ui.ui_videoinfo import Ui_VideoInfoDialog
from db.VideoDB import Video
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMessageBox
from PyQt5.Qt import QTime
import os


class VideoInfoDialog(QDialog):

    def __init__(self, call_type, path, parent=None):

        super(VideoInfoDialog, self).__init__(parent)
        self.call_type = call_type
        self.path = path
        self.ui = Ui_VideoInfoDialog()
        self.db = Video()

        self.ui.setupUi(self)

        self.ui.pathLineEdit.setEnabled(False)

        if self.call_type == "add":
            self.ui.okButton.setEnabled(False)
        elif self.call_type == "edit":

            video_info = self.db.select_video_info_by_path(self.path)[0]
            name = Video.get_video_info_name(video_info)
            start_str = Video.get_video_info_start(video_info)
            end_str = Video.get_video_info_end(video_info)

            self.ui.pathSelectButton.setEnabled(False)
            self.ui.pathLineEdit.setText(self.path)
            self.ui.nameLineEdit.setText(name)
            start = QTime()
            start.setHMS(int(start_str.split(":")[0]), int(start_str.split(":")[1]), int(start_str.split(":")[2]))
            end = QTime()
            end.setHMS(int(end_str.split(":")[0]), int(end_str.split(":")[1]), int(end_str.split(":")[2]))
            self.ui.startTimeEdit.setTime(start)
            self.ui.endTimeEdit.setTime(end)
            self.ui.okButton.setEnabled(True)
        else:
            pass

        self.ui.okButton.clicked.connect(self.confirm)

        self.ui.pathSelectButton.clicked.connect(self.select_file)

        self.ui.cancelButton.clicked.connect(self.close)

    def select_file(self):

        path, file_type = QFileDialog.getOpenFileName(self, "Select File", "." + os.path.sep, "All Files (*)")
        if len(self.db.select_video_info_by_path(path)) != 0:
            QMessageBox.warning(self, "warning", "path: " + path + " is already in the db.")
        else:
            self.ui.pathLineEdit.setText(path)
            name = path.split(os.path.sep)[len(path.split(os.path.sep)) - 1]
            self.ui.nameLineEdit.setText(name)
            self.ui.okButton.setEnabled(True)

    def confirm(self):

        path = self.ui.pathLineEdit.text()
        name = self.ui.nameLineEdit.text()
        start = self.ui.startTimeEdit.text()
        end = self.ui.endTimeEdit.text()
        cost = Video.calculate_video_cost(start, end)

        if self.call_type == "add":
            self.db.insert_video_info(path, name, start, end, cost)
        elif self.call_type == "edit":
            self.db.update_video_info_by_path(path, name, start, end, cost)
        else:
            pass

        self.close()

    def close(self):
        self.db.close()
        super(VideoInfoDialog, self).close()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    v = VideoInfoDialog()
    v.show()

    sys.exit(app.exec_())
