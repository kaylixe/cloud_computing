import connexion
import six

from swagger_server.models.cpu import CPU
from swagger_server.models.disk import DISK
from swagger_server.models.memory import MEMORY
from swagger_server import util
import os, platform, subprocess, re, psutil


def cpu_information():
    platform_info = {
       "Architecture Type": platform.architecture(),
       "Machine Type": platform.machine(),
       "Processor Type": platform.processor(),
       "System Type": platform.system(),
       "Values": platform.uname()
    }
    return platform_info


def disk_count_information():
    countdata = {
        "Read Count": psutil.disk_io_counters.read_count,
        "Write Count": psutil.disk_io_counters().write_count,
    }
    return countdata


def memory_information():
    memorydata = {
       "Active Memory": psutil.virtual_memory().active,
       "Inactive Memory": psutil.virtual_memory().inactive,
       "Cached Memory Used": psutil.virtual_memory().cached
    }
    return memorydata


def get_cpu():
    return cpu_information()


def get_disk():
    return disk_count_information()


def get_memory():
    return memory_information()

