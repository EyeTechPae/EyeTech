{
    "code", 0xA,                    // code number indicating the type of message
                                    // inside of this message
                                    //
                                    // 0xA -> NORMAL message
                                    // 0xB -> ERROR message
    
    "message": "random message",    // Some message sent from the server. May contain relevant
                                    // information the user needs to know

    "error_message": "Some error"   // if this is an error message, this field contains information about
                                    // said error
                                    
    "places": [0, 0, 1, 0, ...]     // array containg one number for each parking spot. A value of 1 indicates
                                    // that the spot is occupied, a value of 0 indicated that the spot is
                                    // available
}
