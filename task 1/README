### Step 1: Hello world
Docker doesn't have the hello-world image yet, so it downloads it, creates a container from it, runs it, and the container exits. You'll see a message starting Hello from Docker!

```bash
docker run hello-world
```

### Step 2: See what's on your machine
docker ps is empty. The container ran and exited, so nothing is running
docker ps -a shows the stopped container, with a randomly generated name

```bash
docker ps              # running containers
docker ps -a           # all containers, including stopped ones
```

### Step 3: Pull another container
You'll see a cow saying your message. Everything after the image name ("Hello Docker") is passed to the program inside the container as an argument.
The first time, Docker downloads the image. Run the same command again and notice that it starts instantly, because the image is now stored locally.

```bash
docker run rancher/cowsay "Hello Docker"
```

### Step 4: Removing stopped containers

Running `docker ps -a` should show you have 2 (or more) stopped containers, one for each docker run. 
Stopped containers hang around until you delete them.
To clean them all up at any point:

```bash
docker container prune
```

### Step 5: Start a web server
You should see web with status Up and the ports column showing 8080->80.

```bash
docker run -d --name web -p 8080:80 nginx
```
- `-d` runs it in the background
- `--name web` gives it a name
- `-p 8080:80` connects port 8080 outside to port 80 inside the container

Confirm it's running. You should get some HTML starting with Welcome to nginx!.

```bash
docker exec web cat /usr/share/nginx/html/index.html
```
To see it in a browser, open the Ports tab at the bottom of VS Code, find port 8080, and Ctrl + Click on the Forwarded Address.

### Step 6: Read a file inside the container
docker exec runs a command inside a running container. This prints the source of the page you just saw

```bash
docker exec web cat /usr/share/nginx/html/index.html
```

### Step 7: Edit that file
Refresh the page in your browser. You should now see I edited this

```bash
docker exec web sh -c 'echo "<h1>I edited this</h1>" > /usr/share/nginx/html/index.html'
```

### Step 8: Destroy the container and start again
docker rm -f forcibly stops and deletes the container. 
The second command creates a brand-new one from the same image.
Refresh the page and you should see the Welcome to nginx screen

```bash
docker rm -f web
docker run -d --name web -p 8080:80 nginx
```

### Step 9: Run nginx with your folder mounted
A bind mount shares a folder from your machine with the container.

- $(pwd)/page	The page folder on your machine ($(pwd) expands to your current directory)
- /usr/share/nginx/html	Where it appears inside the container
- :ro	Read-only: the container can read the files but not change them

Load the page. You should see Hello from my own file.

### Step 10: Make your own changes
Open page/index.html in your editor and change the heading text
Refresh the page, the change should appear

```bash
docker rm -f web
docker run -d --name web -p 8080:80 \
  -v "$(pwd)/page:/usr/share/nginx/html:ro" nginx
```
