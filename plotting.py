import matplotlib.pyplot as plt
from preproccessing1 import *



#a function takes 2 features and plots them together across all 3 classes
def plotting_function(Feature1,Feature2):
    X1 = df_Adelie[Feature1]
    Y1 = df_Adelie[Feature2]
    X2 = df_Gentoo[Feature1]
    Y2 = df_Gentoo[Feature2]
    X3 = df_Chinstrap[Feature1]
    Y3 = df_Chinstrap[Feature2]

    plt.figure(Feature1+' vs. '+Feature2)
    plt.scatter(X1, Y1, color ='red')
    plt.scatter(X2, Y2, color = 'green')
    plt.scatter(X3, Y3, color = 'blue')
    plt.title(Feature1 + ' vs. ' + Feature2+'\n Adelie = red, Gentoo = green, Chinstrap = blue')
    plt.xlabel(Feature1)
    plt.ylabel(Feature2)
    plt.show()

#the plotting of every 2 features
"""plotting_function(feature1,feature2)
plotting_function(feature1,feature3)
plotting_function(feature1,feature4)
plotting_function(feature1,feature5)

plotting_function(feature2,feature3)
plotting_function(feature2,feature4)
plotting_function(feature2,feature5)

plotting_function(feature3,feature4)
plotting_function(feature3,feature5)
plotting_function(feature4,feature5)"""


# plotting after the training
def plotting_function_after(F_one,F_two,w1,w2,B,class1,class2):
    f1 = class1[F_one]
    z1 = class1[F_two]
    f2 = class2[F_one]
    z2 = class2[F_two]

    all_f=pd.concat([f1, f2])
    X1 = all_f.max()
    X2 = all_f.min()

    Y1=(-B-(X1 * w1))/w2
    Y2=(-B-(X2 * w1))/w2

    plt_x=[X1,X2]
    plt_y=[Y1,Y2]
    plt.figure(F_one + ' vs. ' + F_two)
    plt.scatter(f1, z1, color='orange')
    plt.scatter(f2, z2, color='black')

    plt.title(F_one + ' vs. ' + F_two + ' Decision Boundry\n class1 = orange, class2 = black')
    plt.xlabel(F_one)
    plt.ylabel(F_two)

    plt.plot(plt_x,plt_y)

    plt.show()










