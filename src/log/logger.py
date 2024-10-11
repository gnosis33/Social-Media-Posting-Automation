# Pseudocode for Logger Class

# Class Logger:
#     Method __init__(log_file):
#         Initialize log file for logging errors and info

#     Method log_error(message):
#         Write error message to log file

#     Method log_info(message):
#         Write info message to log file

# logger.py file contains the Logger class, which is responsible for logging error and info messages to a log file.
# The Logger class has methods for logging errors and info messages, which write the messages to the log file specified during initialization.
# The Logger class can be used to log information and errors during the execution of the application, providing a record of events for debugging and monitoring purposes.
# The log file path is specified when creating an instance of the Logger class, allowing for flexibility in where the log messages are stored.
# The Logger class will be called by the main application to log messages based on the application's state, errors and events.

# logger.py

class Logger: # Logger class
    def __init__(self, log_file): # Initialize log file for logging errors and info
        self.log_file = log_file

    def log_error(self, message): # Write error message to log file
        with open(self.log_file, 'a') as file:
            file.write(f'ERROR: {message}\n')

    def log_info(self, message): # Write info message to log file
        log_file_path = self.log_file # Specify the path to the log file
        with open(log_file_path, 'a') as file:
            file.write(f'INFO: {message}\n')