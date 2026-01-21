import time

class PerformanceLogger:
    def __init__(self, driver):
        self.driver = driver

    def get_page_load_time(self):
        start = time.time()
        self.driver.execute_script("return document.readyState")
        end = time.time()
        return end - start
