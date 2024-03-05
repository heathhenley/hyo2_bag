import os
import logging
from shutil import copyfile

from hyo2.bag.bag import BAGFile
from hyo2.bag.helper import Helper

logging.getLogger().setLevel(logging.DEBUG)

file_bag_0 = os.path.join(Helper.samples_folder(), "bdb_01.bag")
if not os.path.exists(file_bag_0):
    raise FileNotFoundError(f"the file does not exist: {file_bag_0}")
logging.debug(f"- file_bag_0:\n{file_bag_0}")

file_bag_copy = os.path.join(os.path.dirname(__file__), "tmp_copy.bag")
bag_copy = copyfile(file_bag_0, file_bag_copy)

bag_0 = BAGFile(file_bag_copy, mode="r+")
logging.debug(bag_0)

output_xml = "fixed_metadata.xml"
if not os.path.exists(output_xml):
    raise FileNotFoundError(f"unable to find metadata file: {output_xml}")
bag_0.substitute_metadata(output_xml)
os.remove(output_xml)

bag_0.close()
os.remove(file_bag_copy)
