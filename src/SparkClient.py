from pyspark.sql import SparkSession


class SparkClient():
    ## Note: Taking inspiration from this blog post: ##
    # https://towardsdatascience.com/healthcare-dataset-with-spark-6bf48019892b ## 
    def __init__(self, app_name: str, csv_file_name: str):
        self.app = SparkSession.builder.master('spark://spark:7077').appName(app_name).getOrCreate()
        self.dataset = self.app.read.csv(csv_file_name, inferSchema=True,header=True)
    
    def show_group_data(self, column_name):
        self.dataset.groupBy(column_name).count().show()
        
