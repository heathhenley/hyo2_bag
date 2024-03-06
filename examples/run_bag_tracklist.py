import logging
import os

from hyo2.bag.helper import Helper
from hyo2.bag import tools

logging.getLogger().setLevel(logging.DEBUG)


# verbose + test file
file_bag_0 = os.path.join(Helper.samples_folder(), "bdb_02.bag")
logging.debug(f"# Verbose + test file: {file_bag_0}")
tools.bag_tracklist.main(["-v","-hd", "-o", "test_it.csv", file_bag_0])
logging.debug("")

# verbose + fake file
file_bag_0 = os.path.join(Helper.samples_folder(), "not_present_00.bag")
logging.debug(f"# Verbose + fake file: {file_bag_0}")
tools.bag_tracklist.main(["-v", file_bag_0])
logging.debug("")


# test file
file_bag_0 = os.path.join(Helper.samples_folder(), "bdb_02.bag")
logging.debug(f"# Test file: {file_bag_0}")
tools.bag_tracklist.main([file_bag_0])
logging.debug("")
