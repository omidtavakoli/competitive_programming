import threading
import yaml
from src.logger import logging

"""
Defining a global lock for thread safety
"""
try:
    lock = threading.Lock()
except Exception as exc:
    logging.error(exc.__str__())


class Main(object):
    def __init__(self, conf_file_path):
        """
        A class for wrapping all the work in. This class receives the path of a
        yaml file where the configuration information is stored. After loading
        the file, configurations are will be accessible through `input_dict` property.

        :param conf_file_path: configuration file path (a yaml file)
        """
        self.conf_file_path = conf_file_path
        self.input_dict = self._read_config(file_path=conf_file_path)
        self.running_interval = self.input_dict["global_config"]["check_for_new_projects"]

    def _read_config(self, file_path):
        """
        A private method for loading a yaml file.
        :param file_path: a string representing a valid file path
        :return: a Python dictionary
        """
        logging.warning("Trying to load configuration file.")
        with open(file_path) as stream:
            try:
                return yaml.load(stream)
            except Exception as exc:
                logging.error("Problem in reading the configuration file. " + exc.__str__())

    def recursive_formulation(self, coins, x):
        # page 67
        # coin problem for {c1,c2,...,ck} then f(x) = min (f(x-c1), f(x-c2),...,f(x-ck)) + 1
        # the function can be made efficient by using memoization
        if x < 0:
            # 10^9 denote infinite
            return 1e9
        if x == 0:
            return 0
        u = 1e9
        for i in coins:
            u = min(u, self.recursive_formulation(coins, x - i)+1)
        return u

    def main(self):
        print("main called")
        print(self.recursive_formulation([1, 3, 4], 30))


def run(conf_file_path="conf/default-conf.yml"):
    """
    A procedure (an impure function) for running the objects of class Main
    :param conf_file_path: file path for configuration yaml file
    :return: None
    """
    main_obj = Main(conf_file_path=conf_file_path)
    with lock:
        main_obj.main()
    threading.Timer(interval=main_obj.running_interval, function=run).start()

if __name__ == "__main__":
    """
    Entry point of the program.
    """
    run()
