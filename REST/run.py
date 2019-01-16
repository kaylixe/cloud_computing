from eve import Eve
import psutil
import platform

app = Eve()

@app.route('/processor_info')
def processor_info():

    computer_details = (platform.processor(),
	      platform.processor(),
              platform.machine(),
              platform.version(),
              platform.system(),
	      psutil.cpu_freq(),
              psutil.virtual_memory(),
              psutil.cpu_stats(),
              psutil.virtual_memory(),
              psutil.disk_partitions())
              
    return computer_details

if __name__ == '_main_':
    app.run()