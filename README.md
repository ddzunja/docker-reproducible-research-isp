# DEJAN DZUNJA - Docker for Reproducible Research

Project from Introduction to Data Science course

- Author: Dejan Dzunja (dejan|(dot)|dzunja|(at)|skoltech|(dot)|ru

- Docker image [link](https://hub.docker.com/r/ddzunja/docker-example)

If you have any problems with image, please send me an email!

### How to build and run image

<ol> 
<li> Run "docker build -t image_name ." </li>
<li> Run "docker run -v "$(pwd)/results:/example/results" image_name" - this will mount conrainer's  /example/results directory to ./results directory on your host machine</li>
</ol>
