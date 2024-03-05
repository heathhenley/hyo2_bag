import os
import logging

from hyo2.bag.bag import BAGFile
from hyo2.bag.helper import Helper
from hyo2.bag.meta import Meta

logging.getLogger().setLevel(logging.DEBUG)

file_bag_0 = os.path.join(Helper.samples_folder(), "bdb_01.bag")
if not os.path.exists(file_bag_0):
    raise FileNotFoundError(f"the file does not exist: {file_bag_0}")
logging.debug("- file_bag_0:\n{file_bag_0}")

bag_0 = BAGFile(file_bag_0, mode='r')
logging.debug(bag_0)

meta = Meta(bag_0.metadata())

logging.debug(
    f"vertical datum: {meta.wkt_vertical_datum} ({type(meta.wkt_vertical_datum)})")
