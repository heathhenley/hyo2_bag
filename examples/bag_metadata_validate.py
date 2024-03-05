import os
import logging

from hyo2.bag.bag import BAGFile
from hyo2.bag.helper import Helper


logging.getLogger().setLevel(logging.DEBUG)

file_bag_0 = os.path.join(Helper.samples_folder(), "bdb_01.bag")
if not os.path.exists(file_bag_0):
    raise FileNotFoundError(f"the file does not exist: {file_bag_0}")
logging.debug(f"- file_bag_0:\n{file_bag_0}")

bag_0 = BAGFile(file_bag_0, mode='r')
ret = bag_0.validate_metadata()
logging.debug(f"valid: {ret}")

if not ret:
    for bag_error in bag_0.meta_errors:
        logging.debug(" - %s" % bag_error)