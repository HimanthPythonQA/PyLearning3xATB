import csv
import pandas as pd




class Test_CRUD(object):

    def test_update_1(self):
        #read the file
        with open('EX_JULY/Ex_26072024/userdata.csv') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row[0],row[1])

    def test_update_2(self):
        df = pd.read_csv('EX_JULY/Ex_26072024/userdata.csv')
        print(df)

crud = Test_CRUD()
crud.test_update_1()
crud.test_update_2()