# TIMEWIZARD
### A interactive user-guide 



...TW  is the leading planning and scheduling software for 
Opera houses and Theaters in the Nordic. This site displays a interactive FAQ for users of this programme.
 

## UX

Users of TW learns how to use the software by attending a few lessions with the developers.  There is hardly any user manuals for the programme. If users have questions about this rather complex software they use Teams to chat with the developers and to ask their questions. This means no other customer gets access to these questions -allthough they possibly face the same problems and obstacles. This website is a solution to this problem. 

On this site users can ask their questions as well as read allready asked ones. This is not only a great service for the users -it is also helpful for the developers not having to answer as many questions. 

As progress is made on developing user guides -these can also be accessed on this site.   

#### Wireframe 
This software is used backstage and because of that the color theme is dark grey with blue elements. The Timewizard software actually doesn't have these colors today -it will be implemented in future upgrades. So this site can be considered a mockup for the actual software. Details such as a slide-out nav and accordeons is familiar for TW users, here provided by Materialize. 
User stories and detailed description of Wireframe and UX is found
[here](/static/WireframePetramile3.pdf) or on this site: manuals - web - wireframe. 



## Features
#### User can:
* #### read questions 
The questions is displayed in accordeons -when user clicks on the question the answer is displayed  

* #### ask questions
User fills in a form with:
* username
* select what programme is concerned (as the software has two parts -desktop for administrators and web for regular users).
* question
* date when the problem occured (sometimes a problem is solved with a upgrade or due to a problem with upgrades -therefore this information is important)



* #### edit and delete questions:
this site provides a pen and a garbage can to the accordeon. Press the pen and the filled form opens and can be edited.

* Answer 
On this site it is possible to answer the questions. If the question is answered a icon on the accordeon turns blue. For unanswered questions the same icon is red. This way it is easy for the developers to spot unanswered questions. 

* Switch -Happy with the answer? 
A question can be answered but it's not the same thing as problem solved for the user. This switch will light up a blue thumbs-up icon on the accordeon when selected. If not the same icon will be grey. 

* #### User Manuals
Gives access to pdf:s (target_blank) along with some contact information. 


#### Features Left to Implement
* This site will need a autocomplete search for the questions as well as a filter to sort questions by categories. 

* When answering - make it possible to add a image. 

* Who is answering? Add a chips with that information. 

* Sort the questions with the latest first. 

## Technologies
Timewizard is written in Visual Basic and Angular JS with Devextreme components and SQL. So this site is quite the opposite. These technologies is used:

* Python 3
* Flask
* MongoDB Atlas
* Jquery
* Materialize

## Testing
This site is tested manually for:
* Navbars
This site uses two navbars depending on size. The links in the navbars is tested as well with the change between the different navbars.  
* adding questions
* open and close the accordeon with question
* edit questions
* delete questions
* open pdfs in "target_blank" -checking that all links is working
* two buttons change color depending on user input in the edit form - this is tested. 
* syntax test for the Html-templates is performed with: https://validator.w3.org/

## Deployment
Deployment to Heroku is performed by:
1. Creating a new repository at Heroku
2. Login with the terminal in C9:
```bash
heroku login
```

Then commit to Heroku:
```bash
git remote -v
git add .
git commit -m "header" -m "subject"
git push -u heroku master
```

Deployment to Github is performed by:
1. Creating a new repository at Github
2. Login with the terminal in C9:
```bash
git remote add origin https://github.com/ringarochkryss/timewizard.git
```

Then push the same data to Github as was just sent to Heroku:
```bash
git push -u origin master
```

Also in Heroku it is possible to connect Heroku with Github for syncronization.

To make the app work at Heroku it's important to make a proc-file: 
In the terminal write: 

```bash
echo web: python run.py > Procfile
```

I ran into trouble with commiting the files. This trick solved that problem: 

```bash
sudo chown -R "${USER:-$(id -un)}" .
```
[Thanks to Stack Overflow and mr or mrs Code Worm](https://stackoverflow.com/questions/6448242/git-push-error-insufficient-permission-for-adding-an-object-to-repository-datab)

## Credits
To develop this site obviously I was inspired by the software TW and the developers who just hired me to work on the web part of this programme.


I have followed several turtorials working with Mongo Db and Flask in Visual Studio and Gitpod. 
For instance this one:
[rest-flask-mongodb-heroku](https://spapas.github.io/2014/06/30/rest-flask-mongodb-heroku/ "rest-flask-mongodb-heroku")


This actual site is written using the instructions from [Code Institute](https://codeinstitute.net/ "Code Institute")

 [Materialize](https://materializecss.com/ "Materialize")
provides great instructions on how to use the components. 
It's a bit tricky to escape the color theme in the details -at least without SASS.  [Here](https://www.jquery-az.com/learn-create-materialize-switches-5-examples/ "jquery-az") I found the key for how to make the switch look more decent.



I also took some help from these sites to make the readme look ok:
[makeareadme.com](https://www.makeareadme.com/ "makeareadme.com") & [Markdown-Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#links "Markdown-Cheatsheet")



This is a Code Institute school project -Thankyou to the Tudors and my mentor Seun for all help!