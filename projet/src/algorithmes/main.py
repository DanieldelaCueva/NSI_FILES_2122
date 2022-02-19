from rot13 import rot13_c, rot13_d

string = "On est le 22-01-22"

print(rot13_d(rot13_c(string)["message_code"].lower())["message_decode"])