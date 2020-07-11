#!/usr/bin/env python3
from modules.image_downloader import ImageDownloader

if __name__ == "__main__":
    test_list = [
        "http://goskatalog.ru/muzfo-imaginator/rest/images/original/25346966",
        "http://goskatalog.ru/muzfo-imaginator/rest/images/original/25346972",
        "http://goskatalog.ru/muzfo-imaginator/rest/images/original/25346971",
    ]

    sample_dir = "test"

    img_d = ImageDownloader(test_list)
    img_d.download(sample_dir)
