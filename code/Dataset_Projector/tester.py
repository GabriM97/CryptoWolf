from Dataset_Projector import Dataset_Projector

#TEST CLASS Dataset_Projector - TEST 1
projector=Dataset_Projector ()

x=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20],[21,22,23,24],[25,26,27,28],[29,30,31,32],[33,34,35,36],[37,38,39,40]]
print ("Starting Dataset: {} \n".format(x))

print ("\n")

p=[1,1,0,1]
projection=projector.to_project(x,p)

print ("Projection 1: {} \n".format(p))

print ("Projected Dataset 1: {} \n".format(projection))

#TEST CLASS Dataset_Projector - TEST 2
p=[0,0,0,2]
projection=projector.to_project(x,p)

print ("Projection 2: {} \n".format(p))

print ("Projected Dataset 2: {} \n".format(projection))






