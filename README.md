# DockerPractices
This is the folder where my Docker exercises will be located.

### GuessNumberGame

A random number between 1-50 is kept by the computer. The user tries to find this number according to the answers given by the computer. Returns the number of attempts up to the time found.

*Ex Image*

![Guess Number Game Ex Image](https://github.com/MelihSelamiUrkmezz/DockerPractices/blob/master/GuessNumberGame/ExImage.png)

-> If you want to try the app;

- docker image pull melihselamiurkmez/guessgame
- docker container run --name <containername> -it melihselamiurkmez/guessapp 

### Stream Website with Flask

It is python code that enables publishing a website from Flask.

*Ex Image*

![Website Ex Image](https://github.com/MelihSelamiUrkmezz/DockerPractices/blob/master/FlaskStream/website.png)

-> If you want see my website;

- docker image pull melihselamiurkmez/website
- docker container run --name <containername> -d -p <port>:5000 melihselamiurkmez/website 

### Instagram Automation

It allows you to find unfollowers of yourself or the people you follow on your Instagram account. It also allows to return the url of the profile photo of any desired account.

*Ex Image*

![Instagram Automation Ex Image]()

-> If you want to try the app;

- docker image pull melihselamiurkmez/instagramscript
- docker container run --name <containername> -it melihselamiurkmez/instagramscript
