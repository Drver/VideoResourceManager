from ui.ui_videoresourcemanager import Ui_VideoResourceManagerWidget
from ui.VideoInfoDialog import VideoInfoDialog
from db.VideoDB import Video
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem, QMessageBox, QFileDialog
from PyQt5.Qt import QAbstractItemView

import os
import subprocess


class VideoResourceManager(QWidget):

    def __init__(self, parent=None):
        super(VideoResourceManager, self).__init__(parent)
        self.ui = Ui_VideoResourceManagerWidget()
        self.db = Video()

        self.video_info_table_current_column = None

        self.ui.setupUi(self)

        self.ui.editVideoButton.setEnabled(False)
        self.ui.deleteVideoButton.setEnabled(False)
        self.ui.playVideoButton.setEnabled(False)

        self.ui.addVideoButton.clicked.connect(self.add_video)
        self.ui.editVideoButton.clicked.connect(self.edit_video)
        self.ui.deleteVideoButton.clicked.connect(self.delete_video)
        self.ui.selectPotPlayerPathButton.clicked.connect(self.select_pot_player)
        self.ui.playVideoButton.clicked.connect(self.play_video)
        self.ui.searchVideoButton.clicked.connect(self.search_video)

        self.ui.videoInfoTableWidget.setHorizontalHeaderLabels(["name", "path", "start", "end", "cost"])
        self.ui.videoInfoTableWidget.setColumnWidth(0, 120)
        self.ui.videoInfoTableWidget.setColumnWidth(1, 480)
        self.ui.videoInfoTableWidget.setColumnWidth(2, 80)
        self.ui.videoInfoTableWidget.setColumnWidth(3, 80)
        self.ui.videoInfoTableWidget.setColumnWidth(4, 80)
        self.ui.videoInfoTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.videoInfoTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.videoInfoTableWidget.itemClicked.connect(self.video_info_table_column_selected)
        self.ui.videoInfoTableWidget.itemSelectionChanged.connect(self.video_info_table_column_changed)

        self.refresh_video_info_table()

    def add_video(self):

        self.videoInfoDialog = VideoInfoDialog("add", None)
        self.videoInfoDialog.show()
        self.videoInfoDialog.finished.connect(self.refresh_video_info_table)

    def edit_video(self):

        self.videoInfoDialog = VideoInfoDialog("edit", self.ui.videoInfoTableWidget.item(
            self.video_info_table_current_column, 1).text())
        self.videoInfoDialog.show()
        self.videoInfoDialog.finished.connect(self.refresh_video_info_table)

    def delete_video(self):

        path = self.ui.videoInfoTableWidget.item(self.video_info_table_current_column, 1).text()
        replay = QMessageBox.question(self, "Delete confirm", "Do you want to delete " + path,
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if replay == QMessageBox.Yes:
            self.db.delete_video_info_by_path(path)

        self.refresh_video_info_table()

    def select_pot_player(self):

        path, file_type = QFileDialog.getOpenFileName(self, "Select PotPlay exe", "." + os.path.sep, "All Files (*)")
        self.ui.potPlayerPathDisplayLabel.setText(path)

    def search_video(self):
        search = self.ui.searchVideoLineEdit.text()
        video_info_list = self.db.select_video_info_by_name(search)
        self.set_video_info_table(video_info_list)
        self.ui.searchVideoLineEdit.setText("")

    def play_video(self):

        pot_player_exe_path = self.ui.potPlayerPathDisplayLabel.text()
        if pot_player_exe_path == "" or pot_player_exe_path is None:
            QMessageBox.warning(self, "warning", "Please set PotPlayer exe first!")
            return
        elif not os.path.exists(pot_player_exe_path):
            QMessageBox.warning(self, "warning", pot_player_exe_path + " not exist!")
            return

        path = self.ui.videoInfoTableWidget.item(self.video_info_table_current_column, 1).text()
        start = self.ui.videoInfoTableWidget.item(self.video_info_table_current_column, 2).text()
        cmd = pot_player_exe_path + " " + path + " /seek=" + start

        subprocess.Popen(cmd)

    def refresh_video_info_table(self):

        video_info_list = self.db.select_video_info()
        self.set_video_info_table(video_info_list)

    def set_video_info_table(self, video_info_list):

        self.ui.videoInfoTableWidget.setRowCount(len(video_info_list))
        i = 0
        for video_info in video_info_list:
            new_item = QTableWidgetItem(Video.get_video_info_name(video_info))
            self.ui.videoInfoTableWidget.setItem(i, 0, new_item)

            new_item = QTableWidgetItem(Video.get_video_info_path(video_info))
            self.ui.videoInfoTableWidget.setItem(i, 1, new_item)

            new_item = QTableWidgetItem(Video.get_video_info_start(video_info))
            self.ui.videoInfoTableWidget.setItem(i, 2, new_item)

            new_item = QTableWidgetItem(Video.get_video_info_end(video_info))
            self.ui.videoInfoTableWidget.setItem(i, 3, new_item)

            new_item = QTableWidgetItem(str(Video.get_video_info_cost(video_info)))
            self.ui.videoInfoTableWidget.setItem(i, 4, new_item)

            i = i + 1

    def video_info_table_column_selected(self, item):

        self.video_info_table_current_column = item.row()

        self.ui.editVideoButton.setEnabled(True)
        self.ui.deleteVideoButton.setEnabled(True)
        self.ui.playVideoButton.setEnabled(True)

    def video_info_table_column_changed(self):

        self.ui.editVideoButton.setEnabled(False)
        self.ui.deleteVideoButton.setEnabled(False)
        self.ui.playVideoButton.setEnabled(False)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    v = VideoResourceManager()
    v.show()

    sys.exit(app.exec_())
