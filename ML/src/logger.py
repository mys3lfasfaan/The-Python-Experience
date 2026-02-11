import logging
import os, sys
from datetime import datetime

## IMPORT THE LOGGER WHEREEVER YOU WANT TO USE !
script_name = os.path.basename(sys.argv[0]) 
log_filename = os.path.splitext(script_name)[0] + ".log"

LOG_FILE = f"{log_filename}-{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)



logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] - %(filename)s - %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)