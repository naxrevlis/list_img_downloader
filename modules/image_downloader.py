#!/usr/bin/env python3
import requests
from os import path, mkdir
import re

from requests.exceptions import HTTPError


class Queue:
    def __init__(self, image_list):
        """Initiate simple queue for image_list

        :param image_list:
        :returns:
        :rtype:

        """
        self.queue = image_list

    def get(self):
        if len(self.queue) > 0:
            return self.queue[0]
        return False

    def pop(self):
        if len(self.queue) > 0:
            self.queue = self.queue[1:]

    def lenght(self):
        return len(self.queue)


class ImageDownloader:
    def __init__(self, image_list):
        self.queue = Queue(image_list)
        self.target_folder = None

    def __image_download(self, url):
        try:
            r = requests.get(url)
            file_name = self.__get_filename_from_cd(
                r.headers.get("content-disposition")
            )
            if file_name:
                open(self.target_folder + "/" + file_name, "wb").write(r.content)
            return True
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Python 3.6
        except Exception as err:
            print(f"Other error occurred: {err}")  # Python 3.6

    def __get_filename_from_cd(self, cd):
        """
        Get filename from content-disposition
        """
        if not cd:
            return None
        fname = re.findall("filename=(.+)", cd)
        if len(fname) == 0:
            return None
        return fname[0][1:-1]

    def __check_target_folder(self, folder):
        if path.exists(folder):
            self.target_folder = folder
            return True
        try:
            mkdir(folder)
            self.target_folder = folder
            return True
        except:
            print("Problems creating path. Exiting")
            return False

    def download(self, target_folder):
        if not self.__check_target_folder(target_folder):
            print("Could't download images")
            return False
        if self.queue.lenght == 0:
            print("Image list is empty")
            return False

        while self.queue.lenght() != 0:
            if self.__image_download(self.queue.get()):
                self.queue.pop()
