# FindMeAnImage
An Image Search Application by Garvit Kulshrestha

![Screenshot 2023-09-19 081316](https://github.com/Garvitkul/FindMeAnImage/assets/83578615/b8c53d0c-a7ac-4271-b78d-4266eefe395f)


This project is based on the API of Pexels. You can use it to search the images as per your keywords. It is using Flask as backend. It is available in container form and is ready to deploy application. We are using Flask, Docker, Request Module of Python tools for it.

You can look at the Pexels API documentation - https://www.pexels.com/api/documentation/?language=javascript

Imp - You need to add your API-Key in the app.py code.

index.html should be in the folder named tamplates.
Flask application runs on port 5000.

# Create container from my image in DockerHub

My Docker Image for this Project is available here <br />
https://hub.docker.com/repository/docker/garvitkulshrestha/FindMeAnImage_garvit <br />

You can create a container directly from image. Command to do so is - <br />
sudo docker run -i -t --name FindMeAnImage_garvit -p 5000:5000 garvitkulshrestha/FindMeAnImage_garvit <br />

# Create container from Dockerfile

Imp - Update the Dockerfile with the URL of Github repo which has your API-Key.

Create the Dockerfile as per the content given in my Dockerfile.

Run the below command in the same folder where Dockerfile exists - <br />
sudo docker build -t garvitkulshrestha/FindMeAnImage_garvit_mylocalimage .

Now, your docker image is ready and you can create container from this image using this below command - <br />
sudo docker run -i -t --name FindMeAnImage_garvit -p 5000:5000 garvitkulshrestha/FindMeAnImage_garvit_mylocalimage

# Run the Application

When your container is ready, you can go into your container. <br />
Now, you need to follow the below commands <br />
cd FindMeAnImage
Python3 app.py

Now, your application is running on port 5000. If your Host Machine has a public IP then you can browse your page at PublicIP:5000 otherwise you can browse it on localhost:5000 as well.
