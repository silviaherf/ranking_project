# The DataMad0820 ranking project

![Ironhack logo](https://www.fundacionuniversia.net/wp-content/uploads/2017/09/ironhack_logo.jpg)

This project is developed at the scope of Ironhack's Data Analytics Full-time Bootcamp.



## Resume
![Ranking ](src/ranking.jpg)

The aim of this project is to carry out information about ironhack-datalab's datamad0820 repo, where all students release our labs and tasks over the bootcamp.

The information is requested to Github's API (after signing with key), loaded as bash, cleaned up along that bash's structure and submitted to a just-created MongoDB database in two different collections.

Then further functions and analysis are reported by different self-done API endpoints using Flask.

At last, a Docker image is created, ir order to deploy the API to Heroku afterwards:

https://rankingdatamad0820.herokuapp.com/ 

For the deployment, a MongoDB Atlas virtual collection is assigned, so that data is not removed by Heroku.

The whole project is defined to be runned from the terminal.


## Structure

1) README.txt: As a resume for the content of the project an its development

2) data_to_json.py: This file imports the information needed from Github API and exports it to a locally saved bash file

3) server.py:  It defines the local server where the self-done API will be executed.

4) src: It contains relevant files so that the script can be runned. These are .py files:
    4a) data_exportation.py-> It contains every function that the data_to_bash needs so as to clean and fix up the requested data from Github API.
    4b) data_toMongo.py-> This script generates two new collections in MongoDB (students and labs) from the bash file exported in the file above
    4c) database.py-> It defines the new database in MongoDB that will be created and used to export the previously commented collections
    4d) api_gen.py-> It defines the endpoints of the self-created API



## Endpoints preview
At the created API, the following endpoints are defined:


### **/**

This is just the first view of the API

```bash

"Welcome to the DataMad0820 Ranking API!!!"
```

### **/student/create/<studentname>**

    - Purpose: This endpoint creates a student document and saves into MongoDB students collection. It also updates a student document in MongoDB if it     already exists
    - Params: the student's name in Github (his nickname)
    - Queryparams:  any parameter needed by the user
    - Returns: the generated id for that document in MongoDB

```bash

{
_id: {
$oid: "5f6dce76a1e5af306a824187"
}
}
```

### **/student/all**

    - Purpose: List all students in database
    - Returns: An array of student objects   
    
```bash

[
"AnaMA96",
"CarlosSanzDGP",
"Daniel-GarciaGarcia",
"Davidlazarog",
"DiegoCaulonga",
"Diegon8",
"FDELTA",
"IreneLopezLujan",
"Jav1-Mart1nez",
"Joycelili",
"KevsDe",
"PaulaNuno",
"VanessaMacC",
"bmedm",
"charliesket",
"gontzalm",
"grundius1",
"jmena23",
"jorge-alamillos",
"laura290",
"marta-zavala",
"miguelgimenezgimenez",
"prueba",
"rfminguez",
"silviaherf"
]
```    

### **/lab/create**
        
    This endpoint acts both with GET or POST method. For POST method, it does not work in any web browser, it must be opened with Postman or similar
 
    - Purpose:  This endpoint creates a lab document and saves into MongoDB labs collection. It also updates a lab document in MongoDB if it already exists
    - Params: The lab-prefix to be analyzed (its name). Example: lab-scavengers
    - Returns: the generated id for that document in MongoDB



```bash

{
_id: {
$oid: "5f6dced4a1e5af306a824188"
}
}
```



### **/lab/<lab_prefix>/search**

    -Purpose: Returns lab analysis
    -Params: lab_prefix->the name of the lab we want information about. Example: lab-scavengers
    -Returns: Number of open PR
            Number of closed PR
            Percentage of completeness (closed vs open)
            The number of missing PR from students
            The list of unique url of memes used for that lab
            Instructor correction time in hours


```bash
{
-The number of opened PR is: 0,
-The number of closed PR is: 22,
The percentage of completeness is: 100,
Number of missing PR is: 0,
Distinct memes: [
"https://user-images.githubusercontent.com/52798316/93581456-7b2fc300-f9a1-11ea-89d2-a953d5c73e88.png",
"https://user-images.githubusercontent.com/57899051/93586847-3e67ca00-f9a9-11ea-8465-1adf354977db.jpg",
"https://user-images.githubusercontent.com/57899051/93983317-b146bb80-fd82-11ea-9258-7c6fc9cc4bae.jpg",
"https://user-images.githubusercontent.com/57899051/93983568-0a165400-fd83-11ea-8897-3a4ecda0498d.jpg",
"https://user-images.githubusercontent.com/57899051/93996013-01794a00-fd92-11ea-991f-a84941b9f87f.jpg",
"https://user-images.githubusercontent.com/57899051/94000575-a21e3880-fd97-11ea-97e6-5911358b321e.jpg",
"https://user-images.githubusercontent.com/57899051/94006365-034a0a00-fda0-11ea-816c-0d37a003fe02.jpg",
"https://user-images.githubusercontent.com/57899051/94072832-bb0a0680-fdf6-11ea-98c0-218bb341e298.jpg",
"https://user-images.githubusercontent.com/57899051/94084085-f4e20980-fe04-11ea-81c4-629cd7d6a515.jpg",
"https://user-images.githubusercontent.com/57899051/94084536-0ed01c00-fe06-11ea-9798-16036b8611cf.jpg",
"https://user-images.githubusercontent.com/57899051/94084735-8bfb9100-fe06-11ea-8adf-68df497feaba.jpg",
[
"https://user-images.githubusercontent.com/52798316/93581456-7b2fc300-f9a1-11ea-89d2-a953d5c73e88.png"
]
],
Instructors mean grade time in hours: [
{
_id: "ferrero-felipe",
correction_time: 95.50999999999999
},
{
_id: "agalvezcorell",
correction_time: 139.43699999999998
}
]
}
```


### **/memeranking**

    -Purpose: This function returns the most ussed meme for datamad0820 for each lab

```bash

[
{
_id: {
category: "https://user-images.githubusercontent.com/57899051/92761970-78761200-f392-11ea-9407-19db1bd89d8a.jpg"
},
name: "lab-web-scraping"
},
{
_id: {
category: "https://user-images.githubusercontent.com/57899051/93326119-a20ebd80-f818-11ea-899a-b1c3d3ce6a6c.jpg"
},
name: "lab-parsing-api"
},
{
_id: {
category: "https://user-images.githubusercontent.com/57899051/91450439-99ac0e00-e87c-11ea-8567-6f6e0cc24ce0.png"
},
name: "lab-mysql-select"
},
{
_id: {
category: "https://user-images.githubusercontent.com/57899051/91437288-f2be7680-e869-11ea-9090-90ced9135e4b.jpg"
},
name: "lab-mysql-select"
},
... }]
```

### **/lab/<lab_prefix>/meme**

    -Purpose: Get a random meme (extracted from the ones used for each student pull request) for that lab.
    -Params: The lab-prefix to be analyzed (its name). Example: lab-scavengers
    -Returns: a random meme

```bash

[
{
meme1: "https://user-images.githubusercontent.com/52798316/93581456-7b2fc300-f9a1-11ea-89d2-a953d5c73e88.png"
}
]
```