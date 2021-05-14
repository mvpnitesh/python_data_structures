"""
Find the most common friend in a social_network
"""

class SocialNetwork:
    def __init__(self, name, friends=None):
      self.name = name
      self.friends = friends
      self.next = None
      
class SocialNetworkList:
    def __init__(self, head):
        self.head = head

def suggest_a_friend(user, social_network_list):
    social_network_user = social_network_list
    friend_suggestions = []
    most_common_friends_count = 0
    most_comman_friend = None
    while(social_network_user != None):
        if (user.name != social_network_user.name):
            new_friends = social_network_user.friends
            user_friends = user.friends
            if social_network_user not in user_friends:
                count_common_friends = 0
                for i in user_friends:
                    if i in new_friends:
                        count_common_friends+=1
                if count_common_friends >= 1:
                    if most_common_friends < count_common_friends:
                        most_common_friends_count = count_common_friends
                        most_comman_friend = social_network_user.name
        else:
            pass
        social_network_user = social_network_user.next
    
    return most_comman_friend