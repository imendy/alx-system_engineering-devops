## Design of a Three-Server Web Infrastructure for www.foobar.com:

Here's the design of a three-server web infrastructure to host the website www.foobar.com, addressing the specified requirements:

1. Server 1 (Load Balancer):

Role: Load Balancer
Components: HAproxy
Explanation: The load balancer distributes incoming user requests across multiple servers to ensure optimal resource utilization, enhance fault tolerance, and improve scalability.
2. Server 2 (Web and Application Server):

Role: Web Server (Nginx), Application Server
Components: Nginx, Application Files (Code Base)
Explanation: This server handles incoming requests, serves static content directly, and forwards dynamic requests to the application server. The application server processes dynamic content and generates responses based on user requests.
3. Server 3 (Database Cluster):

## Role: Database (MySQL) - Primary and Replica nodes
Components: MySQL Primary Node, MySQL Replica Node
Explanation: The database cluster utilizes a Primary-Replica (Master-Slave) setup to enhance data availability, fault tolerance, and read scalability.
Distribution Algorithm of Load Balancer (HAproxy):
The load balancer uses a Round Robin distribution algorithm. This algorithm cycles through the available servers sequentially, evenly distributing incoming requests to each server in a circular order.

## Active-Active vs. Active-Passive Setup:
The load-balancer configuration enables an Active-Passive setup. In this setup, one server actively handles user requests (Active), while the other server stands by as a backup (Passive). This ensures high availability and instant failover in case the active server experiences issues.

## Database Primary-Replica Cluster:
The Primary-Replica cluster consists of a Primary (Master) database node and one or more Replica (Slave) database nodes. The Primary node handles write operations (inserts, updates, deletes), while Replica nodes replicate data from the Primary and handle read operations. Replication keeps the Replica nodes in sync with the Primary to enhance data redundancy and availability.

## Difference Between Primary and Replica Nodes:

Primary Node: Responsible for handling write operations. It's the authoritative source for data changes and modifications.
Replica Node: Handles read operations, offloading traffic from the Primary. It replicates data from the Primary and ensures that data is consistent for read-heavy operations.
Issues with the Infrastructure:

Single Point of Failure (SPOF): The load balancer can become a SPOF. If it fails, traffic distribution and failover would be affected.

Security Issues: There's no mention of a firewall or HTTPS in the design, leaving the infrastructure vulnerable to security threats and data breaches.

No Monitoring: Lack of monitoring tools means there's no insight into server performance, resource usage, or potential issues.

To address these issues, implementing a redundant load balancer, setting up firewalls and HTTPS, and integrating monitoring solutions would be crucial steps.
