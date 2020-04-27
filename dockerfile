#基础镜像
FROM base_lcow:v1.0
  
#语言编码设置
RUN localedef -c -f UTF-8 -i zh_CN zh_CN.utf8
ENV LC_ALL zh_CN.UTF-8
  
  
#将项目目录文件复制到镜像中,CODE_DIR是在基础镜像中定义的
COPY . $CODE_DIR/
  
  
#安装项目依赖包
RUN pip3 install -r $CODE_DIR/requirements.txt
  
#暴露端口
EXPOSE 8080
  
  
#启动项目
CMD ["python3.7", "/home/jeroen/project/py/CIMS/manage.py", "runserver", "0.0.0.0:8080"]