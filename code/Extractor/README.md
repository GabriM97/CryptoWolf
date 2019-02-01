v1.0{

- Dataset_Maker: now create a "Numpy Dataset".
- Cleaner: clean the features. Added Feature_Scaling and Mean_Normalization methods.
- Dataset_Creator: now the dataset creation is more easier thanks to create_dataset() method. Added Dataset Split method and Dataset Saving methods.
- Tester: added method to test the new Dataset Creation.
- More details for each component in the files.

}


v0.5{

-Added following classes:
1. JSON_Saver: allows to extract and save in JSON files all candlestick of a Market from a timestamp.
2. Dataset_Maker: creates a pair of matrices for each candlestick period; This two matrices will be our Dataset.
3. Dataset_Creator: helps to create the Dataset. You only need to execute the method run_all() or run_only_maker() with the chosen candlestick period.

-tester.py is now more modular and new methods were added to tests the new classes.
-More details for each component in the files.

}



v0.4{

-Added a method ,into Time_Stamp_Converter class, that converts a timestamp into a date and time , expressed in local timezone.
-Fixed ohlc method logic on Extractor class
-Fixed retrieve_data method on Extractor class, now error handling is right
-Periods_Maker, this class helps you to make right "periods" paramiter for ohlc method of Extractor Class
-Reorganization of Tests

}

v0.3 {

-Fix data type returned from convert method of Time_Stamp_Converter Class, now data type returned is ready for the Extractor Library Calls.

}

v0.2 {

-Fix for Time_Stamp_Converter Class, now you can convert a date-time with a non-fixed time

}

v0.1 {

-Extractor Class is the Python Implementation of CryptoWatch REST API
-Code is entirely English commented
-The Time_Stamp_Converter Class allow you to convert a date-time into a UNIX Timestamp (time is per default 00:00:00), that is the right format for some calls of the Extractor library

}