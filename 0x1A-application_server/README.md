# 0x1A. Application server
## Concepts
For this project, students are expected to look at these concepts:
* [Web Server](https://intranet.hbtn.io/concepts/17)

* [Server](https://intranet.hbtn.io/concepts/67)

* [Web stack debugging](https://intranet.hbtn.io/concepts/68)
![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/9/c7d1ed0a2e10d1b4e9b3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220224%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220224T083834Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b2e9556e53e3a4cc0e1ad3b5647e2d73ff833c22f7f22e5728d00cd3f6fa288f) 

## Background Context
[](https://youtu.be/pSrKT7m4Ego)

Your web infrastructure is already serving web pages via   ` Nginx `   that you installed in your  [first web stack project](https://intranet.hbtn.io/rltoken/RrbqMLWOJUyVaWdXsnpvXw) 
 . While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your   ` Nginx `   and make is serve your Airbnb clone project.
## Resources
Read or watch :
* [Application server vs web server](https://intranet.hbtn.io/rltoken/RerpYBxsgrpIorHjbDgulw) 

* [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](https://intranet.hbtn.io/rltoken/uosy5QXdMbDPA1tFTR1eoA) 
 (As mentioned in the video, do not install Gunicorn using  ` virtualenv ` , just install everything globally)
* [Running Gunicorn](https://intranet.hbtn.io/rltoken/QTnnkj6vfQV9ovW_eYWWDQ)

* [Be careful with the way Flask manages slash](https://intranet.hbtn.io/rltoken/whE8do28ZiJJoJLyb1ACwA) 
 in [route](https://intranet.hbtn.io/rltoken/JLjrXD4MLS3rUkQr5QyxtA)
  -  ` strict_slashes `
* [Upstart documentation](https://intranet.hbtn.io/rltoken/rldSTo2ZFS8clyTHH3SyBg)
