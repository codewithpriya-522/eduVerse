import logging

def getlogger(config):
   
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
   
    output_type = config.get("logger","output_type", fallback="console")
   
    match output_type:
        case "file":
            fh = logging.FileHandler(config.get("logger","file_name"))
            fh.setLevel(logging.DEBUG)
            fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
            logger.addHandler(fh)
        case "console":
            ch = logging.StreamHandler()
            ch.setLevel(logging.DEBUG)
            ch.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
            logger.addHandler(ch)
        case _:
            print("Invalid Logger Type")
    return logger