import os

class Runner:
    def __init__(self, script):
        self.script = script

    def start(self):
        try:
            exit_code = os.system(f'python {self.script}')
            if exit_code != 0:
                print(f"Error starting {self.script}. Exit code: {exit_code}")
        except Exception as e:
            print(f"An unexpected error occurred while running {self.script}: {e}")

# Define the scripts
server = "server.py"
api = "api.py"

# Create instances and run
server_runner = Runner(server)
server_runner.start()

api_runner = Runner(api)
api_runner.start()
