#Import libraries

import petl as etl

import pandas as pd

import cdata.oracleoci as mod
 
cnxn = mod.connect("User=Hrmcv;Password=#455@34!204;Server=localhost;Port=1521;")
 
sql = "SELECT CompanyName, City FROM Customers WHERE Country = 'US'"
 
table1 = etl.fromdb(cnxn,sql)
 
table2 = etl.sort(table1,'City')
 
etl.tocsv(table2,'customers_data.csv')
 
table3 = [ ['CompanyName','City'], ['NewCompanyName1','NewCity1'], ['NewCompanyName2','NewCity2'], ['NewCompanyName3','NewCity3'] ]

 
etl.appenddb(table3, cnxn, 'Customers')