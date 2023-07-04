import random
import sys

# To get the number of friends
def get_num_friends():
    while True:
        num_friends = int(input("Enter the number of friends joining (including you):\n"))
        if num_friends <= 0:
            print("No one is joining for the party")
            sys.exit(0)
        else:
            return num_friends

# To get the names of friends
def get_friend_names(num_friends):
    if num_friends > 0:
        print("Enter the name of every friend (including you), each on a new line:\n")
        friends= []
        for i in range (num_friends):
            friend = input()
            friends.append(friend)
        return friends
    return None

# To split the bill
def bill_splitter(total_bill, num_friends):
    return round(total_bill / num_friends , 2)

# To choose our lucky guy
def get_lucky_guy(friends):
    is_lucky = input("""Do you want to use the "Who is lucky?" feature? Write Yes/No:\n""")
    if (is_lucky.lower() == "yes"):
        lucky_guy = random.choice(friends)
        friends.remove(lucky_guy)
        return lucky_guy
    return None

# To calculate the bill
def calculate_bill(num_friends, total_bill, lucky_guy, friends):
    split_bill = bill_splitter(total_bill, len(friends))
    friends_dict = {friend : split_bill for friend in friends}
    if lucky_guy:
        friends_dict[lucky_guy] = 0
        print(f"{lucky_guy} is the lucky one!")
    else:
        print("No one is going to be lucky")
    return friends_dict

# To print the bill
def print_bill(friends_dict):
    print(friends_dict)

def main():
    num_friends = get_num_friends()
    friends = get_friend_names(num_friends)
    total_bill = float(input("Enter the total bill value:\n"))
    lucky_guy = get_lucky_guy(friends)
    friends_dict = calculate_bill(num_friends, total_bill, lucky_guy, friends)
    print_bill(friends_dict)

if __name__ == "__main__":
    main()








