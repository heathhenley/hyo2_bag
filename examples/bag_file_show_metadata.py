import logging
import os

from hyo2.bag.bag import BAGFile
from hyo2.bag.helper import Helper

logging.getLogger().setLevel(logging.DEBUG)

file_bag_0 = os.path.join(Helper.samples_folder(), "bdb_01.bag")
if not os.path.exists(file_bag_0):
  raise FileNotFoundError(f"the file does not exist: {file_bag_0}")
logging.debug("- file_bag_0: %s" % file_bag_0)

bag_0 = BAGFile(file_bag_0, mode="r")
bag_0.populate_metadata()

logging.debug("- bag_0.metadata: %s" % bag_0.metadata())