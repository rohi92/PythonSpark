def strongPasswordChecker(self, password):
    if len(password) >= 6 and any(map(str.isdigit, password)) and (not password.islower() and not password.isupper()):
        return 0
    else:
        if (len(password) <= 6):
            return 6 - len(password)
        elif (len(password) >= 6 and not (any(map(str.isdigit, password))) and not (
                not password.islower() and not password.isupper())):
            return 2
        else:
            return 1
if __name__=="__main__":
    a = strongPasswordChecker("self", "1337C0d3")