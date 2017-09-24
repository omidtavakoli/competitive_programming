import logging


try:
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s  %(levelname)-8s %(message)s',
                        datefmt='%Y-%m-%d,%H:%M:%S',
                        filename='logs/default-log',
                        filemode='w')
    logging.getLogger('elasticsearch').setLevel(logging.CRITICAL)
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

except Exception as exc:
    print(exc.__str__())
