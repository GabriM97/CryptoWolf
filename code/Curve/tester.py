from Curve import Curve
from sklearn.linear_model import LinearRegression

#TEST CLASS Curve - plot_2D_H	
obj=Curve()

regressor=LinearRegression()
x=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20],[21,22,23,24],[25,26,27,28],[29,30,31,32],[33,34,35,36],[37,38,39,40]]
y=[50,32,93,40,62,150,96025,45,30,690]

regressor.fit(x,y)
theta_0 = regressor.intercept_
theta_1_4 = regressor.coef_
print (theta_0)
print (theta_1_4.shape)

obj.plot_2D_H (x,y,regressor,"1")

#TEST CLASS Curve - plot_3D_H	

obj.plot_3D_H (x,y,regressor,"2")

#TEST CLASS Curve - plot_degree_graphic

degree=[1,2,3,4,5]
j_train=[1000,850,550,350,250]
j_cv=[1200,1100,1050,1400,1600]
idx=[0,1,2,3,4]
obj.plot_degree_graphic (degree,j_train,j_cv,idx)





