#!/usr/bin/env python

import voltron
from voltron.core import Client


def main():
    # Create a client and connect to the server
    client = Client()
    client.connect()

    # Main event loop
    while True:
        # Wait for the debugger to stop again
        res = client.perform_request('wait')
        if res.is_success:
            # If nothing went wrong, get the instruction pointer and print it
            res = client.perform_request('registers', registers=['rip'])
            if res.is_success:
                print("Instruction pointer is: 0x{:X}".format(res.registers['rip']))
            else:
                print("Failed to get registers: {}".format(res))
        else:
            print("Error waiting for the debugger to stop: {}".format(res))
            break


if __name__ == "__main__":
    main()