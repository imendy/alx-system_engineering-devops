## Design of a Secured and Monitored Three-Server Web Infrastructure for www.foobar.com:

## Here's the design of a three-server web infrastructure that addresses the specified requirements:

## 1. Server 1 (Load Balancer):

Role: Load Balancer, SSL Termination
Components: HAproxy, SSL Certificate
Explanation: The load balancer distributes incoming requests and terminates SSL. It ensures secure communication by decrypting SSL traffic and forwarding requests to backend servers in plain HTTP.
## 2. Server 2 (Web and Application Server):

Role: Web Server (Nginx), Application Server
Components: Nginx, Application Files (Code Base)
Explanation: This server handles incoming requests, serves static content directly, and forwards dynamic requests to the application server. It also enforces HTTPS for communication with users.
## 3. Server 3 (Database Cluster):

Role: Database (MySQL) - Primary and Replica nodes
Components: MySQL Primary Node, MySQL Replica Node
Explanation: The database cluster employs a Primary-Replica setup for data redundancy, availability, and scalability.

## Additional Elements and Explanations:

1. Firewalls:
Firewalls are added to each server to control incoming and outgoing traffic, enforcing security policies and protecting against unauthorized access and cyber threats.

2. SSL Certificate (HTTPS):
Traffic is served over HTTPS using an SSL certificate. This encrypts the data exchanged between users and the website, ensuring confidentiality and integrity of sensitive information.

3. Monitoring Clients:
Monitoring clients are deployed on each server to collect performance data, logs, and metrics. These clients send data to a monitoring service like Sumo Logic, helping administrators gain insights into system health and performance.

Monitoring Purpose and Data Collection:
Monitoring is used to track the health, performance, and availability of the infrastructure. Monitoring clients collect data on server metrics (CPU usage, memory, disk), application logs, response times, and other key indicators. This data helps identify issues, troubleshoot problems, and ensure optimal performance.

Monitoring Web Server QPS:
To monitor web server QPS (Queries Per Second), you can configure monitoring clients to track incoming request counts over time. This data can be aggregated and visualized to understand traffic patterns and load trends.

## Issues with the Infrastructure:

Terminating SSL at Load Balancer:
Terminating SSL at the load balancer level can expose decrypted traffic within the internal network, potentially compromising security. It's better to maintain end-to-end encryption by offloading SSL at the backend server level.

Single MySQL Server for Writes:
Relying on a single MySQL server for write operations is risky. If that server fails, write availability is lost. A primary-replica cluster provides redundancy and failover.

 Identical Servers with All Components:

Having identical servers for web, application, and database components can lead to resource contention and inefficient resource utilization. Separating specialized roles can improve performance and scalability.

By addressing these issues and implementing the suggested changes, the infrastructure can achieve a higher level of security, reliability, and scalability.
