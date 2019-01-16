import default_controller


def cpu_get():
    return controller.cpu_information()


def disk_get():
    return controller.disk_count_information()


def memory_get():
    return controller.memory_information()

