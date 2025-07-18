import argparse
import json

"""
    Compares your followers list to your following list and prints out who is not following you back. 
"""

# Create the parser
parser = argparse.ArgumentParser(description="Follower and Following lists")

# Add arguments
parser.add_argument("followers_file", type=str, help="Name of file containing followers list")
parser.add_argument("following_file", type=str, help="Name of file containing the following list")

args = parser.parse_args()

#Path/name to files
followers_file = args.followers_file
following_file = args.following_file

followers_list = {} # dict for O(1) access by username
following_usernames = []  # list of usernames you're following

with open(followers_file) as file:
    data = json.load(file)
    for user in data:
        username = user['string_list_data'][0]['value']
        followers_list[username] = username

# Load following file and build list
with open(following_file) as file:
    data = json.load(file)
    data = data['relationships_following']
    for user in data:
        username = user['string_list_data'][0]['value']
        following_usernames.append(username)

# Find people you follow who do NOT follow you back
not_following_back = []

for username in following_usernames:
    if username not in followers_list:
        not_following_back.append(username)

# Print the users not following you back
print("Users not following you back:")
for i,user in enumerate(not_following_back):
    print(f'{i+1}: {user}' )
























