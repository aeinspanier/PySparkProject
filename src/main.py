from SparkClient import SparkClient
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("echo")
    args = parser.parse_args()
    print(args.echo)
    client = SparkClient('stroke', 'mounted-data/healthcare-dataset-stroke-data.csv')
    client.show_group_data('stroke')
