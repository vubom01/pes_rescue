FROM mysql:5.7
ENV MYSQL_ROOT_PASSWORD root
# tên database
ENV MYSQL_DATABASE pet-rescue
ENV MYSQL_USER huuvuot
ENV MYSQL_PASSWORD huuvuot
# thêm file sql vào cơ sở dữ liệu
ADD pes_rescue.sql /docker-entrypoint-initdb.d
#set port cho cổng truy cập
EXPOSE 3307