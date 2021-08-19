'''
class EGY:
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    r_values = list(range(0,1700))

    df = pd.read_excel('values.xlsx', engine='openpyxl')
    y1 = list(df['ONE'].values)
    y2 = list(df['TWO'].values)
    y3 = list(df['THREE'].values)
    plt.plot(r_values, y3, label='SVM + SUB-LEACH')
    plt.plot(r_values, y2, label='SUB-LEACH')
    plt.plot(r_values, y1, label='LEACH')
    plt.legend()
    plt.show()
'''

class EGY:
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    x = list(range(0,1700))

        df = pd.read_excel('mon 9 aug.xlsx', engine='openpyxl')
        y1 = list(df['o1'].values)
        y2 = list(df['h22'].values)
        y3 = list(df['t123'].values)
    plt.xlabel('Number of Rounds')
    plt.ylabel('Alive Nodes/Sensors')
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.plot(x, y3)
    plt.show()

    data = {'Leach':1000, 'Sub-Leach':1550, 'SVM+Leach':1700}
    model = list(data.keys())
    values = list(data.values())
    
    fig = plt.figure(figsize = (10, 5))
    

    plt.bar(model, values, color ='maroon',
            width = 0.4)
    
    plt.xlabel("model type")
    plt.ylabel("Number of rounds")
    plt.title("performance of models")
    plt.show()

    data1 = {'Leach':40, 'Sub-Leach':100, 'SVM+Leach':100}
    model1 = list(data1.keys())
    values = list(data1.values())
    
    fig = plt.figure(figsize = (10, 5))
    

    plt.bar(model1, values, color ='red',
            width = 0.3)
    
    plt.xlabel("model type")
    plt.ylabel("alive nodes")
    plt.title("number of alive nodes after 900 rounds")
    plt.show()

    ## difference between subleach and proposed model actually came after 1500 rounds

    data2 = {'Leach':0, 'Sub-Leach':40, 'SVM+Leach':40}
    model2 = list(data2.keys())
    values = list(data2.values())
    
    fig = plt.figure(figsize = (10, 5))
    

    plt.bar(model2, values, color ='blue',
            width = 0.1)
    
    plt.xlabel("model type")
    plt.ylabel("alive nodes")
    plt.title("number of alive nodes after 1500 rounds")
    plt.show()




EGY()