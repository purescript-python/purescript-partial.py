def crashWith():
    def ap_msg(msg):
        return Exception(msg)

    return ap_msg
