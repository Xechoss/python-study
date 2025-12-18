import random
import time
from threading import Thread
from concurrent.futures import ThreadPoolExecutor


def download(*, file_name):
    start = time.time()
    print(f'开始下载{file_name}……')
    time.sleep(random.randint(2, 6))
    end = time.time()
    print(f'完成下载{file_name}……')
    print(f'下载时长: {end - start:.3f}秒.')


class DownloadThread(Thread):

    def __init__(self, file_name):
        self.file_name = file_name
        super().__init__()

    def run(self) -> None:
        start = time.time()
        print(f'开始下载{self.file_name}……')
        time.sleep(random.randint(2, 6))
        end = time.time()
        print(f'完成下载{self.file_name}……')
        print(f'下载时长: {end - start:.3f}秒.')


def main():
    # threads = [
    #     Thread(target=download, kwargs={'file_name': 'Python从入门到入土.pdf'}),
    #     Thread(target=download, kwargs={'file_name': 'MySQL从删库到跑路.avi'}),
    #     Thread(target=download, kwargs={'file_name': 'Linux从精通到放弃.mp4'})
    # ]

    threads = [
        DownloadThread('Python从入门到入土.pdf'),
        DownloadThread('MySQL从删库到跑路.avi'),
        DownloadThread('Linux从精通到放弃.mp4')
    ]

    with ThreadPoolExecutor(max_workers=4) as pool:
        file_names = ['Python从入门到入土.pdf', 'MySQL从删库到跑路.avi', 'Linux从精通到放弃.mp4']
        start = time.time()
        for file_name in file_names:
            pool.submit(download, file_name=file_name)
    end = time.time()
    print(f'总耗时: {end - start:.3f}秒.')

    start = time.time()
    # 启动三个线程
    for thread in threads:
        thread.start()
    # 等待线程结束
    for thread in threads:
        thread.join()
    end = time.time()
    print(f'总耗时: {end - start:.3f}秒.')


if __name__ == '__main__':
    main()
