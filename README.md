<h3>Task1:</h3>
Create 2 docker images:
<lo>
<li>python flask app + uwsgi </li>
<li>mysql with persistent volume</li>
</lo>
Create docker network for connecting two containers

<h3>Task1 Resolution:</h3>
<lo>
<li>git clone git@github.com:AlexandrVovk/mentor-prog-docker-task1.git && cd mentor-prog-docker-task1</li>
<li>docker network create external</li>
<li>docker network create internal --internal</li>
<li>docker run -d --name mysql --network internal  -v $(pwd)/init:/docker-entrypoint-initdb.d -v $(pwd)/db:/var/lib/mysql -e MYSQL_DATABASE=app -e MYSQL_ROOT_PASSWORD=my-secret-pw mysql:5</li>
<li>docker build -t mentor_prog_task1_app</li>
<li>docker run -d --name app --network external -p 80:5000 -v $(pwd)/app:/app mentor_prog_task1_app</li>
<li>docker network connect internal app</li>
<li>curl localhost</li>
</lo>

<h5>If you insert new data to database, you will have new output in app</h5>
docker exec -i  mysql mysql -uroot -pmy-secret-pw --database='app' -e 'INSERT INTO app_table ( text ) VALUES ("Hello YourName");'


<h3>Task2:</h3>
Do the same as above with docker-compose.

<h3>Task2 Resolution:</h3>
<lo>
<li>git clone git@github.com:AlexandrVovk/mentor-prog-docker-task1.git && cd mentor-prog-docker-task1</li>
<li>docker-compose up -d</li>
<li>docker exec -i  mysql-compose mysql -uroot -pmy-secret-pw --database='app' -e 'INSERT INTO app_table ( text ) VALUES ("Hello YourName");'</li>
<li>curl localhost</li>
</lo>
