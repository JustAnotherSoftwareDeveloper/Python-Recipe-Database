
# Personal Recipe Database

There are a lot of recipes on the internet. Unfortunately, most of them are bad. I currently store a bunch of recipes in catgorized folders. Probem is that many dishes fit multiple categories. For example: falafel can both be snack food and a meal. The plan here is to have a project that stores pdfs and uses mongo to tag the metadata. then I can use a get request to perform queries and find recipes that fit a specific tag. 

## To Run 

1) Checkout this directory to a specified location 

2) Setup a Mongo instance. I made mine using https://docs.docker.com/samples/library/mongo/ . You'll need to create a recipes collection and point the url at the correct IP

3) Install packages denoted in requirements.txt

4) Run flask and start inserting some recipes.


Note: This is more of a hobby project to improve my skills as a developer than a fully fleged project with continued development. That being said, feel free to ask me any questions. 

