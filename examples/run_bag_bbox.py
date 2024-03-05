import logging
import os

from hyo2.bag.helper import Helper
from hyo2.bag import tools

logging.getLogger().setLevel(logging.DEBUG)

# verbose + test file
file_bag_0 = os.path.join(Helper.samples_folder(), "bdb_01.bag")
logging.debug(f"# Verbose and test file: {file_bag_0}")
tools.bag_bbox.main(["-v", "-o", "test_it.kml", file_bag_0])
logging.debug(f"")

# verbose + fake file
file_bag_0 = os.path.join(Helper.samples_folder(), "not_present_00.bag")
logging.debug(f"# Verbose and fake file: {file_bag_0}")
tools.bag_bbox.main(["-v", file_bag_0])
logging.debug(f"")


# test file
file_bag_0 = os.path.join(Helper.samples_folder(), "bdb_01.bag")
logging.debug(f"# Test file: {file_bag_0}")
tools.bag_bbox.main([file_bag_0])
logging.debug(f"")

