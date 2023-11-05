import socket
import threading
import os
import time

def find_available_port():
    """ This function finds and returns an available port number on the local machine by creating a temporary
        socket, binding it to an ephemeral port, and then closing the socket. """

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s.getsockname()[1]
    
    
def launch_chrome_with_remote_debugging(chrome_path, port, url, history_folder = "remote-profile"):
    """ Launches a new Chrome instance with remote debugging enabled on the specified port and navigates to the
        provided url """

    def open_chrome():
        remote_profile_path = os.path.join(os.getcwd(), history_folder)
        # print("asdfasd",remote_profile_path)
        chrome_cmd = f"{chrome_path} --remote-debugging-port={port} --user-data-dir={remote_profile_path} {url}"
        print(chrome_cmd)
        os.system(chrome_cmd)

    chrome_thread = threading.Thread(target=open_chrome)
    chrome_thread.start()

def wait_for_human_verification():
    print("You need to manually complete the log-in or the human verification if required.")

    while True:
        user_input = input(
            "Enter 'y' if you have completed the log-in or the human verification, or 'n' to check again: ").lower()

        if user_input == 'y':
            print("Continuing with the automation process...")
            break
        elif user_input == 'n':
            print("Waiting for you to complete the human verification...")
            time.sleep(5)  # You can adjust the waiting time as needed
        else:
            print("Invalid input. Please enter 'y' or 'n'.")