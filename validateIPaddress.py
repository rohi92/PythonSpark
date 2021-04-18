def validIPAddress(self, IP):
    """
    :type IP: str
    :rtype: str
    """
    if "." in IP:
        add = IP.split(".")
        if len(add) != 4:
            return "Neither"
        for item in add:
            if not item.isdigit():
                return "Neither"
            if len(item) == 0:
                return "Neither"
            elif int(item) > 255 or int(item) < 0:
                return "Neither"
            elif len(item) > 1 and item[0] == "0":
                return "Neither"
        return "IPv4"
    else:
        add = IP.split(":")
        if len(add) != 8:
            return "Neither"
        for item in add:
            item = item.upper()
            if len(item) == 0 or len(item) > 4:
                return "Neither"
            else:
                for ch in item:
                    if ord(ch) < 47 or ord(ch) > 70:
                        return "Neither"
                    elif ord(ch) < 65 and ord(ch) > 57:
                        return "Neither"
    return "IPv6"


if __name__=="__main__":
    print(validIPAddress("self", "2001:0db8:85a3:0:0:8A2E:0370:7334:"))
