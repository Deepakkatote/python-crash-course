current_users = ["admin","Deepak","Dhruvi","Krushna","Didu"]
new_users = ["admin","Dhruvi","Raju","Ravi","CSK"]
for new_user in new_users:
    if new_user in current_users:
        print(f"username {new_user} is already has been used")
    else:
        print(f"{new_user} is availabel")