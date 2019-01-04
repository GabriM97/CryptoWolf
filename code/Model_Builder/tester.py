from Model_Builder import Model_Builder

#TEST CLASS Model_Builder
builder=Model_Builder ()

#TEST CLASS Model_Builder - load_models
data=builder.load_models()
list_of_lists=data['Models']
print ("List of Lists: {} ".format(list_of_lists))

print ("")

#TEST CLASS Model_Builder - build and print_last_list
x=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20],[21,22,23,24],[25,26,27,28],[29,30,31,32],[33,34,35,36],[37,38,39,40]]
list_of_list=builder.build(x)
print ("")
print (list_of_list)

print ("")

#TEST CLASS Model_Builder - save_models
builder.save_models()





