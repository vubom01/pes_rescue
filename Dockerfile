FROM mysql:latest
ENV MYSQL_ROOT_PASSWORD root
# tên database
ENV MYSQL_DATABASE pet_rescue
ENV MYSQL_USER huuvuot
ENV MYSQL_PASSWORD huuvuot
# thêm file sql vào cơ sở dữ liệu
ADD pet_rescue.sql /docker-entrypoint-initdb.d
#set port cho cổng truy cập
EXPOSE 3306