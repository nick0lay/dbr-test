import argparse
import os

def main(args):
    print("Task 1: Hello World!")
    print("Db name: ", args.db_name)
    print("Prefix: ", args.prefix)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Hyperparameters sent by the client are passed as command-line arguments to the script.
    parser.add_argument('--db_name', type=str, default="veriff_events")
    parser.add_argument('--prefix', type=str, default="test")
    
    # Add more parameters as needed

    args, _ = parser.parse_known_args()
    main(args)