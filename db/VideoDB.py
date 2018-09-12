import sqlite3
import os


class Video:

    def __init__(self):

        self.db_name = '.' + os.path.sep + 'video.db'
        self.video_info_table_name = 'video_info'

        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS " + self.video_info_table_name +
                            " (`path` TEXT, `name` TEXT, `start` TEXT, `end` TEXT, `cost` INTEGER)")

    def close(self):
        self.cursor.close()
        self.conn.close()

    @staticmethod
    def calculate_video_cost(start: str, end: str):
        return (int(end.split(':')[0]) * 3600 + int(end.split(':')[1]) * 60 + int(end.split(':')[2])) - \
               (int(start.split(':')[0]) * 3600 + int(start.split(':')[1]) * 60 + int(start.split(':')[2]))

    def insert_video_info(self, path: str,
                          name: str,
                          start: str,
                          end: str,
                          cost: int):

        if len(self.select_video_info_by_path(path)) == 0:

            self.cursor.execute("INSERT INTO " + self.video_info_table_name +
                                " (`path`, `start`, `end`, `cost`, `name`) VALUES (?, ?, ?, ?, ?)",
                                (path, start, end, cost, name))
            self.conn.commit()

    def update_video_info_by_path(self, path: str,
                                  name: str or None,
                                  start: str or None,
                                  end: str or None,
                                  cost: str or None):

        sql = "UPDATE " + self.video_info_table_name + " SET `path` = '" + path + "' "
        if start is not None:
            sql = sql + " , `start` = '" + start + "' "
        if end is not None:
            sql = sql + " , `end` = '" + end + "' "
        if cost is not None:
            sql = sql + " , `cost` = " + str(cost)
        if name is not None:
            sql = sql + " , `name` = '" + name + "' "
        sql = sql + " WHERE `path` = '" + path + "'"

        self.cursor.execute(sql)
        self.conn.commit()

    def delete_video_info_by_path(self, path:str):

        sql = "DELETE FROM " + self.video_info_table_name + " WHERE `path` = '" + path + "'"

        self.cursor.execute(sql)
        self.conn.commit()

    def select_video_info_by_path(self, path: str):
        self.cursor.execute("SELECT * FROM " + self.video_info_table_name + " WHERE `path` = '" + path + "'")
        return self.cursor.fetchall()

    def select_video_info_by_name(self, name: str):
        self.cursor.execute("SELECT * FROM " + self.video_info_table_name + " WHERE `name` LIKE '%" + name + "%'")
        return self.cursor.fetchall()

    def select_video_info(self):
        self.cursor.execute("SELECT * FROM " + self.video_info_table_name)
        return self.cursor.fetchall()

    @staticmethod
    def get_video_info_path(video_info):
        return video_info[0]

    @staticmethod
    def get_video_info_name(video_info):
        return video_info[1]

    @staticmethod
    def get_video_info_start(video_info):
        return video_info[2]

    @staticmethod
    def get_video_info_end(video_info):
        return video_info[3]

    @staticmethod
    def get_video_info_cost(video_info):
        return video_info[4]


if __name__ == '__main__':
    pass
