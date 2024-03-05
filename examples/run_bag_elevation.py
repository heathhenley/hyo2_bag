import logging
import subprocess
import os

from hyo2.bag.helper import Helper
from hyo2.bag import tools

logging.getLogger().setLevel(logging.DEBUG)


# verbose + test file
file_bag_0 = os.path.join(Helper.samples_folder(), "bdb_01.bag")
logging.debug(f"# Verbose and test file: {file_bag_0}")
tools.bag_elevation.main(["-v", "-o", "test_elv.tiff", file_bag_0])
tools.bag_elevation.main(
  ["-v", "-o", "test_elv.ascii", "-f", "ascii", file_bag_0])
logging.debug("")

# verbose + fake file
file_bag_0 = os.path.join(Helper.samples_folder(), "not_present_00.bag")
logging.debug(f"# Verbose and fake file: {file_bag_0}")
tools.bag_elevation.main(["-v", file_bag_0])
logging.debug("")

# test file
file_bag_0 = os.path.join(Helper.samples_folder(), "bdb_01.bag")
logging.debug(f"Test file: {file_bag_0}")
tools.bag_elevation.main([file_bag_0])
logging.debug("")
