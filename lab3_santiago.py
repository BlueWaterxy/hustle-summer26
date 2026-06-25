# Santiago | Lab 3 | RED
# Ticket 1
# I predict that this would print 9 charcters 
username="BlueWater"
print(len(username))
print(username[0])
print(username[8])
# It's minus one since the index starts at 0, therefore making the last charcter index 8
# Ticket 2 
print("Welcome to Loop, @" + username + "!")
# The method that felt easier was to use the + sign due to being able to add the variable and a text
# username[0] = "X" use as comment since I didn't want to show up on the terminal. 
# What I think it means for a string to be immutable is that you cannot change it.
# Ticket 3 
# PREDICT: I predict that this would print three feed and show up as 2 like 0,1,2
feed = [
    "BLUEPHEW",
    "ISHERE",
    "OVERWATCH"
]
print(feed)
print(feed[0])
# EXPLAIN: The Index I used to to get the first item in the list is 0. Since lists start at 0.
# Ticket 4
# PREDICT:I predict the fourth feed will be showed as 3.
feed.append("HELLO WORLD")
print(feed)
# EXPLAIN: The post index is 3 since the list starts at 0.
# Ticket 5
# PREDICT: The feed that will get removed is the first feed is BLUEPHEW.
feed.pop(0)
print(feed)
# EXPLAIN: The two methods that I use to remove the first item in the list is pop,
# EXPLAIN: and using 0 to remove the first item in the list.
# Ticket 6
# PREDICT: The fowers it will print is nothing due to it being to 0 due to the profile set to 0 on line 44.
profile ={ 
    "username": "BlueWater",
    "followers": 100,
    "verifed": False

}
print(profile["followers"])
#  File "/Users/bluewater/Desktop/untitled folder/Hustle-summer 2026/lab3_santiago.py", line 42, in <module>
    # profile[0]
    # ~~~~~~~^^^
    # EXPLATION: Disctionaries are not indexed by numbers, but by keys instead becasue it has no order.
    # Ticket 7 
    # PREDICT:Age will get an error due to nothing being set to it.
profile["followers"] = profile["followers"] + 50
profile["bio"] = "BLUE"
print(profile)
print(profile.get("age"))
# EXPLAIN: Get is safe due to it being to just grab the value and not being set back by the profile.
# Ticket 8
# PREDICT:@BlueWater has 150 followers and 3 posts. Top post: BLUEPHEW
print(f"@{profile['username']} has {profile['followers']} followers and {len(feed)} posts. Top post: {feed[0]}")
# EXPLAIN: All the data structures that I used in this lab are lists and dictionaries.
