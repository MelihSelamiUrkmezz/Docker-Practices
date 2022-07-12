# Melih Selami Urkmez

import instaloader
from instaloader import Profile
print("Please enter your instagram username:")
Username=str(input())
print("Please enter your instagram password:")
Password=str(input())

L=instaloader.Instaloader()
L.login(Username,Password)

print("Enter instagram account name:")
name=str(input())

profile = Profile.from_username(L.context,name)
print("Processing\n1)Print Unfollowers\n2)Download profile picture\n")

print("Enter your choose:")

choose=int(input())

if(choose==1):
     followees= [i.username for i in profile.get_followees()]
     followers= [i.username for i in profile.get_followers()]

     unfollowers=open("unfollowers.txt","w")

     unfollowers.write(name+ "'s unfollowers\n")

     for x in followees:
        if(not x in followers):
            print(x+"\n")
            unfollowers.write(x)
            unfollowers.write("\n")


     unfollowers.close()

elif(choose==2):

    url=profile.get_profile_pic_url()
    print(url)

else:
    print("Invalid choose!")

print("Process is succesfuly!")

