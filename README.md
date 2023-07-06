# MINISAT-VM PROVISIONING

A Virtual Machine provisioning tool using MiniSat, a centralized open-source tool to manage an organization’s assets by provisioning, maintaining, and updating the hosts on the cloud throughout the complete lifecycle. 

Tools: Eclipse IDE, Node JS, LDAP protocol for authentication, Docker containers, Flask framework

### About: 

The algorithm used in this project helps us to work different managing and monitoring tools together in one platform and to put to efficient usage. To be able to login application with LDAP authentication on the application. Users should be able to provision hosts with different providers such as libvirt, docker container, etc. It should be able to configure network and storage and select the type of provider, type of operating system, and contents. Multimedia content hosted throughout the Internet. Edge resources would be required for both computation and data storage to address the wide data distribution. The necessary edge resources could be dedicated resources spread across content distribution networks.

### Summary:

The application consists of all three modules under one application. The three modules are LDAP authentication, health monitoring, content management, and also host provisioning. More work remains to be done to be full as the scalability of a system's runtime and detection performance in a much longer environment. The existing minisat is an open-source managing and provisioning monitoring tool for virtual machines and docker containers built on Django Web Framework. It has a dashboard to toggle the current state of virtual machines and containers. It has VM provisioning with a kickstart which makes the initialization of the guest operating system interactive. It maps the container port to the host port making the service available outside the container.

### Modules design:
![image](https://user-images.githubusercontent.com/126736660/228868963-8d2e4259-f116-4de6-bdfe-3c28b0641b1c.png)

LDAP Authentication:
![image](https://user-images.githubusercontent.com/126736660/228869091-1f1c3ee4-fd45-42f7-abca-42d68466b010.png)

Add other things later!
Service Level Programming:
![image](https://user-images.githubusercontent.com/126736660/228869427-a60d2a25-9631-4335-a7e5-79f590f20e86.png)

### Output screenshots:

![image](https://user-images.githubusercontent.com/126736660/228870164-bdcadae2-92e4-4a16-8e33-c111eeda2873.png)
![image](https://user-images.githubusercontent.com/126736660/228870226-c3d1c0ae-845f-4f09-97e1-6e0746384f46.png)
![image](https://user-images.githubusercontent.com/126736660/228870253-810d2906-1017-404a-88df-81af7e83460e.png)
![image](https://user-images.githubusercontent.com/126736660/228870272-5d4c10b1-7965-4c7c-bd4d-483964f9455f.png)
![image](https://user-images.githubusercontent.com/126736660/228870298-583af6f8-c69d-458a-9f95-dfcda61914f5.png)
![image](https://user-images.githubusercontent.com/126736660/228870321-865f5a1e-c363-4f5a-b6e2-c50ecc18ee0d.png)
![image](https://user-images.githubusercontent.com/126736660/228870335-c44edc36-d99b-4a99-89c8-d14377dc2bd4.png)

### Various testing used:
 
 - Performance testing
 - Black box testing
 - Unit testing
 - Python testing 
 
### Future Work:
 
In the future, this application can even be used on virtualized systems. More things can be used to manage the systems. Already in the existing system, there are various modules or tools which help in managing, monitoring, content management, etc. But in this project, we collaborate these various tools into one portal. From this, we can develop more and use it on more complex systems and applications. This can be made more efficient and proper in  a convenient way. In this, we are managing a system but in the future, we can develop it to such an extent that one system can be run with the help of the other. With the growing demand for resource utilization, we provision virtual machines so that many operating systems function together along with monitoring. All these virtualized VMs are connected to one main system in this project. Only the main person knows that the systems are being monitored and has the right to authenticate them. It even has health monitoring to enable notifications and alerts to the main system.
