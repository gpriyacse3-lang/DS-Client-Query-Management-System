from login import register_user, login_user

# register test users (run only once)
register_user("client1", "client123", "Client")
register_user("support1", "support123", "Support")

print("Users registered")


# test login
print(login_user("client1", "client123"))
print(login_user("support1", "support123"))
