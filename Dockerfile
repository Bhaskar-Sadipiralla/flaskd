FROM  ubuntu:18.04
RUN apt-get update -y && apt-get upgrade -y && apt-get install git -y && apt-get install unzip -y
WORKDIR /opt
RUN apt install python3-pip -y
RUN  apt install python3-flask -y
RUN pip3 install mysql-connector-python
RUN  apt-get install mysql-server -y
RUN  apt-get install libmysqlclient-dev -y
RUN pip3 install flask-mysqldb
RUN git clone https://github.com/Bhaskar-Sadipiralla/flaskvm.git
WORKDIR /opt/flaskvm
RUN mkdir templates
RUN mv flask_main flask_main.py
RUN mv form.html templates
RUN mv users.html templates
ENTRYPOINT [ "python3" ]

CMD [ "flask_main.py" ]
