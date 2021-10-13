<h3>Task1:</h3>
Create 2 docker images:
<lo>
<li>python flask app + uwsgi </li>
<li>mysql with persistent volume</li>
</lo>
Create docker network for connecting two containers

docker network create external\
docker network create internal --internal\
docker run -d --name mysql --network internal  -v $(pwd)/init:/docker-entrypoint-initdb.d -v $(pwd)/db:/var/lib/mysql -e MYSQL_DATABASE=app -e MYSQL_ROOT_PASSWORD=my-secret-pw mysql:5\
docker build -t mentor_prog_task1_app\
docker run -d --name app --network external -p 5000:5000 -v $(pwd)/app:/app mentor_prog_task1_app\
docker network connect internal app

<h5>If you insert new data to database, you will have new output in app</h5>
docker exec -i  mysql mysql -uroot -pmy-secret-pw --database='app' -e 'INSERT INTO app_table ( text ) VALUES ("Hello YourName");'
