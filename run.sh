docker create -it -p 8082:8080 \
       -v /root/CIMS:/home/jeroen/project/py/CIMS \
       -v /root/databases/lcow:/home/jeroen/project/py/CIMS/databases 5a9bf9e727ec
