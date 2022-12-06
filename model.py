
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from plotting import plotting_function_after
from preproccessing1 import *
import random
from sklearn.metrics import accuracy_score


F = df[df['species'] == 1 ]
S = df[df['species'] ==-1 ]
T = df[df['species'] == 2 ]

First_50  = F[['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g','gender']]
Secound_50= S[['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g','gender']]
Third_50  = T[['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g','gender']]

C1=F['species']
C2=S['species']
C3=T['species']

weight1 =  random.random()
weight2 =  random.random()

global selected_class1,selected_class2
####################### inputs will be  added from the GUI #########################
#F_one='gender'
#F_two='bill_depth_mm'
#C_one='Adelie'
#C_two='Gentoo'

L=0.1
ep=200
B=7
MSE = 0.1
c=["Adelie" , "Gentoo"  ,"Chinstrap" ]
f=["bill_length_mm","bill_depth_mm","flipper_length_mm","gender","body_mass_g"]


####################### inputs will be  added from the GUI #########################
def input_user(x_class,y_feature,lr,e,ba,m):
    global ep ,B ,L ,MSE
    i=0
    c_num=[]
    f_num=[]
    ####get_selsct_class###
    for n in x_class:
        if n.get()==1:
            c_num.append(i)
        i = i+1
    i=0
    ####get_selsct_feature###
    for n in y_feature:
        if n.get()==1:
            f_num.append(i)
        i = i+1
    ###check_bais###
    if ba==1 :
        B = random.random()
    else:
        B = 0

    L   = lr
    ep  = e
    MSE = m
    ################################################################################################################
    F_one = f[f_num[0]]
    F_two = f[f_num[1]]
    C_one = c[c_num[0]]
    C_two = c[c_num[1]]
    if C_one == 'Adelie':
        F_X_train, F_X_test, F_Y_train, F_Y_test = train_test_split(First_50[[F_one, F_two]], C1, test_size=0.4,
                                                                    train_size=0.6, random_state=10)
        class1 = F
        if C_two == 'Gentoo':
            S_X_train, S_X_test, S_Y_train, S_Y_test = train_test_split(Secound_50[[F_one, F_two]], C2, test_size=0.4,
                                                                        train_size=0.6, random_state=10)
            class2 = S
        else:
            C3.replace(2, -1, inplace=True)
            S_X_train, S_X_test, S_Y_train, S_Y_test = train_test_split(Third_50[[F_one, F_two]], C3, test_size=0.4,
                                                                        train_size=0.6, random_state=10)
            class2 = T

    elif C_one == 'Gentoo':
        F_X_train, F_X_test, F_Y_train, F_Y_test = train_test_split(Secound_50[[F_one, F_two]], C2, test_size=0.4,
                                                                    train_size=0.6, random_state=10)
        class1 = S
        if C_two == 'Adelie':
            S_X_train, S_X_test, S_Y_train, S_Y_test = train_test_split(First_50[[F_one, F_two]], C1, test_size=0.4,
                                                                        train_size=0.6, random_state=10)
            class2 = F
        else:
            C3.replace(2, 1, inplace=True)
            S_X_train, S_X_test, S_Y_train, S_Y_test = train_test_split(Third_50[[F_one, F_two]], C3, test_size=0.4,
                                                                        train_size=0.6, random_state=10)
            class2 = T

    else:
        C3.replace(2, 1, inplace=True)
        F_X_train, F_X_test, F_Y_train, F_Y_test = train_test_split(Third_50[[F_one, F_two]], C3, test_size=0.4,
                                                                    train_size=0.6, random_state=10)
        class1 = T

        if C_two == 'Adelie':
            C1.replace(1, -1, inplace=True)
            S_X_train, S_X_test, S_Y_train, S_Y_test = train_test_split(First_50[[F_one, F_two]], C1, test_size=0.4,
                                                                        train_size=0.6, random_state=10)
            class2 = F
        else:
            S_X_train, S_X_test, S_Y_train, S_Y_test = train_test_split(Secound_50[[F_one, F_two]], C2, test_size=0.4,
                                                                        train_size=0.6, random_state=10)
            class2 = S

    #########################################################################
    X_train = pd.concat([F_X_train, S_X_train], ignore_index=True)
    Y_train = pd.concat([F_Y_train, S_Y_train], ignore_index=True)
    x_train_one = X_train[F_one]
    x_train_two = X_train[F_two]
    ##########################################################################
    X_test = pd.concat([F_X_test, S_X_test], ignore_index=True)
    Y_test = pd.concat([F_Y_test, S_Y_test], ignore_index=True)
    x_test_one = X_test[F_one]
    x_test_two = X_test[F_two]
    #####################################################################################
    W1, W2 , Bais   = Training(x_train_one, x_train_two, Y_train, B, weight1, weight2, ep, L,MSE)
    correct, TN, TP = Testing(x_test_one, x_test_two, Y_test, Bais, W1, W2, ep)
    FP = 20 - TN
    FN = 20 - TP
    accuracy = (correct / (40)) * 100
    print(f'Accuracy = ', accuracy, '%')
    print(f'TN = ', TN)
    print(f'FP = ', FP)
    print(f'FN = ', FN)
    print(f'TP = ', TP)

    #---plotting----
    plotting_function_after(F_one,F_two, W1, W2, Bais,class1,class2 )

    return accuracy, TN, FP, FN, TP,W1,W2


###################################################################################
def activation_function(z):
  if z > 0 :
    return 1
  else:
    return -1
####################################################################################

def Training(x1,x2,y,B,w1,w2,epochs,eta,MSE) :
      for epoch in range(epochs):
            for n in range(60):
                net = (w1*x1[n])+(w2*x2[n])+B
                # using linear fun instead of signum fun #
                y_predict = net
                error = y[n] - y_predict
                w1 = w1 + eta * (error*x1[n])
                w2 = w2 + eta * (error*x2[n])
                B  = B  + eta * (error*1)
            for i in range(60):
              net = (w1*x1[i])+(w2*x2[i])+B
              y_predict = net
              error = y[i] - y_predict
              if i == 0 :
                e_mse=(error*error*0.5)
              else:
                e_mse = e_mse + (error*error*0.5)

            e_mse=e_mse/60
            #print(e_mse)
            if e_mse <= MSE :
               return w1,w2,B
               break
            else:
              e_mse=0
              continue
      return w1,w2,B


####################################################################################

def Testing(x1,x2,y,B,w1,w2,epochs) :
    for n in range(40):
        if n==0 :
            count = 0
            count_TN = 0
            count_TP = 0
        net = (w1 * x1[n]) + (w2 * x2[n]) + B
        y_predict = activation_function(net)
        error = y[n] - y_predict
        if error == 0:
            count = count + 1
            if(y[n]==1) :
                count_TN= count_TN+1
            else:
                count_TP =count_TP+1

    return count ,count_TN ,count_TP

####################################################################################






