import logging
import subprocess
import os

from hyo2.bag.helper import Helper
from hyo2.bag import tools

logging.getLogger(__name__).setLevel(logging.DEBUG)

tools_folder = os.path.abspath(os.path.dirname(tools.__file__))
tool_path = os.path.join(tools_folder, 'bag_bbox.py')
logging.debug("tool: %s" % tool_path)

# help
logging.debug("\n\n# -h")
subprocess.call("python %s -h" % tool_path)

# verbose + test file
file_bag_0 = os.path.join(Helper.samples_folder(), "bdb_01.bag")
logging.debug("# -v %s" % file_bag_0)
subprocess.call("python %s -v -o test_it.kml %s" % (tool_path, file_bag_0))

# verbose + fake file
file_bag_0 = os.path.join(Helper.samples_folder(), "not_present_00.bag")
logging.debug("# -v %s" % file_bag_0)
subprocess.call("python %s -v %s" % (tool_path, file_bag_0))

# test file
file_bag_0 = os.path.join(Helper.samples_folder(), "bdb_01.bag")
logging.debug("# %s" % file_bag_0)
subprocess.call("python %s %s" % (tool_path, file_bag_0))
