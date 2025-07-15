---
author: owner
title: Install MySQL and phpMyAdmin using Docker in Ubuntu
date: 2025-07-14
categories: [Programming Language, SQL]
tags: [ ]     # TAG n ames should always be lowercase
description: A step-by-step guide to install MySQL and phpMyAdmin using Docker on Ubuntu. # add some description here
math: true # optional
image:
  path: "assets/headers/mysql-phpmyadmin-cover.png"
--- 
 

In this post, we'll walk through how to install <kbd>MySQL</kbd> and <kbd>phpMyAdmin</kbd> using Docker on Ubuntu.  
This guide follows the YouTube tutorial: [How to install MySQL and phpMyAdmin with Docker on Ubuntu](https://www.youtube.com/watch?v=WoI4AQ1faDg)

## ✅ Install Docker

First, ensure Docker is properly installed. If it isn’t, follow these steps:

### 1. Set Up Docker's `apt` Repository

```bash
# Update and install prerequisites
sudo apt-get update
sudo apt-get install ca-certificates curl

# Add Docker’s official GPG key
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add Docker repository to apt sources
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
````

### 2. Install Docker Engine & Compose

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### 3. Verify the Installation

```bash
# Check Docker version
docker --version
# -> Docker version 28.3.2, build 578ccf6

# Check Docker Compose version
sudo docker compose version
# -> Docker Compose version v2.38.2
```


## 🛠️ Create Docker Compose File

Create a `docker-compose.yml` file with the following content:

```yaml
services:
  phpmyadmin:
    image: phpmyadmin:latest
    container_name: phpmyadmin
    ports:
      - 8080:80
    environment:
      - PMA_ARBITRARY=0
      - PMA_HOST=db
    restart: unless-stopped
    depends_on:
      - db

  db:
    image: mysql:latest
    container_name: mysql
    ports:
      - 3306:3306
    environment:
      MYSQL_ROOT_PASSWORD: mypassword
    restart: unless-stopped
    volumes:
      - dbdata:/var/lib/mysql

volumes:
  dbdata:
```


## 🚀 Run Docker Compose

Now launch the services in the background:

```bash
sudo docker compose up -d
```

Expected output:

```
[+] Running 4/4
 ✔ Network phpmyadmin_default Created
 ✔ Volume "phpmyadmin_dbdata" Created
 ✔ Container mysql Started
 ✔ Container phpmyadmin Started
```


## 🌐 Access phpMyAdmin

Open your browser and visit:

```
http://localhost:8080/
```

Login credentials:

* **Username:** `root`
* **Password:** `mypassword`

You should see the phpMyAdmin login page:

![phpMyAdmin login](assets/posts/phpmyadmin.png)

After login, you can run SQL queries through the main interface:

![phpMyAdmin interface](assets/posts/phpmyamdin-interface.png)


Now you're ready to manage your MySQL database using a simple web UI.