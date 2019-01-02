v1.3{

-Added a method ,into Time_Stamp_Converter class, that converts a timestamp into a date and time , expressed in local timezone.
-Fixed ohlc method logic on Extractor class
-Fixed retrieve_data method on Extractor class, now error handling is right
-Periods_Maker, this class helps you to make right "periods" paramiter for ohlc method of Extractor Class
-Reorganization of Tests

}

v1.2 {

-Fix data type returned from convert method of Time_Stamp_Converter Class, now data type returned is ready for the Extractor Library Calls.

}

v1.1 {

-Fix for Time_Stamp_Converter Class, now you can convert a date-time with a non-fixed time

}

v1.0 {

-Extractor Class is the Python Implementation of CryptoWatch REST API
-Code is entirely English commented
-The Time_Stamp_Converter Class allow you to convert a date-time into a UNIX Timestamp (time is per default 00:00:00), that is the right format for some calls of the Extractor library

}
