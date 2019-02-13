USER MANUl - LEARN.PY

This program allow you to train a List of Model in order to choose the model which fit data in the best way.

At first start, the program ask to the user the Training settings:

1.Download/Update Data from the Internet - This parameter allows user to download fresh data from the internet or use the local Data

2.Plot Graphics - This parameter allows user to plot or not the Training Graphics

3.Model List - This parameter allows user to choose the Models List to train (i.e. restricted list or Full list)

4.PCA Application - This parameter ,in some cases, allows user to apply PCA technique to the Dataset

After the Training parameters choices, program prints the Model list chosen by user and train all Models.

After this, program plots graphic (if it's the case) and then it prints all Models Errors together to the Final Error (calculated on the Test Set) of the Best Model on Training phase.

Moreover, the program saves the best model information in 2 pkl files in order to perform a future inference.
