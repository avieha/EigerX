import doctest
import mysql.connector


def priceCheck(products: list, productPrices: list, productSold: list, soldPrice: list) -> int:
    """
    :param products: list of product names
    :param productPrices: list of price per product
    :param productSold: name of product that was sold
    :param soldPrice: price sold by product sold
    :return: number of price errors
    >>> priceCheck(products=['eggs', 'milk', 'cheese'], productPrices=[2.89, 3.29, 5.79],
    ...                 productSold=['eggs', 'eggs', 'cheese', 'milk'],
    ...                 soldPrice=[2.89, 2.99, 5.97, 3.29])
    2
    >>> priceCheck(products=['rice', 'sugar', 'wheat', 'cheese'],
    ...           productPrices=[16.89, 56.92, 20.89, 345.99],
    ...           productSold=['rice', 'cheese'],
    ...           soldPrice=[18.99, 400.89])
    2
    >>> priceCheck(products=['rice'],
    ...           productPrices=[16.89],
    ...           productSold=['rice', 'rice','rice','rice'],
    ...           soldPrice=[16.89,16.98,0,18.99])
    3
    """
    counter = 0
    for soldIndex, soldProduct in enumerate(productSold):
        if soldPrice[soldIndex] != productPrices[products.index(soldProduct)]:
            counter += 1
    return counter


def digit_summer(num):
    """
    :param num: given number
    :return: sum of digits
    >>> digit_summer(2347623)
    27
    >>> digit_summer(123)
    6
    >>> digit_summer(111)
    3
    >>> digit_summer(0)
    0
    >>> digit_summer(00000)
    0
    """
    if int(num) == 0:
        return 0
    digit = num % 10
    num = int(num / 10)
    return digit + digit_summer(num)


def sql_department():
    """
    :return:
    >>> sql_department()
    ('Executive', 2)
    ('Technical', 2)
    ('Production', 1)
    """
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="mydatabase"
    )

    mycursor = mydb.cursor()

    # mycursor.execute("CREATE DATABASE mydatabase")
    # mycursor.execute('''CREATE TABLE IF NOT EXISTS EMPLOYEE (ID integer primary key,
    #         NAME varchar(100),SALARY integer,DEPT_ID varchar(125))''')
    # mycursor.execute('''CREATE TABLE IF NOT EXISTS DEPARTMENT (ID integer primary key,
    #         NAME varchar(100),LOCATION varchar(125))''')
    # mycursor.execute("SHOW TABLES")
    # mycursor.execute('''INSERT INTO DEPARTMENT(ID,NAME,LOCATION)
    #      VALUES (5,'Management','Paris')''')
    # mydb.commit()

    mycursor.execute('''SELECT department.name,COUNT(*) as num_of_employees 
    FROM employee
    INNER JOIN department ON department.id=employee.dept_id
    GROUP BY employee.dept_id,name
    ORDER BY COUNT(*) DESC''')

    for x in mycursor:
        print(x)

    mycursor.close()
    mydb.close()
    return


if __name__ == '__main__':
    failures, tests = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
