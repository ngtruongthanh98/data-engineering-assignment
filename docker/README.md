### Image pull

`sudo docker pull mcr.microsoft.com/mssql/server:2022-latest`

### Setup container

`sudo docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=Aa123456!" -v ~/Desktop/data-engineering-assignment \ -p 1433:1433 --name sql2 --hostname sql2 \ -d \ mcr.microsoft.com/mssql/server:2022-latest`

### Access database

`docker exec -it sql2 /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P 'Aa123456!'`

### Import data files

`USE [master] `
`GO`
`CREATE DATABASE production ON `
`( FILENAME = ~/Desktop/data-engineering-assignment/database/AdventureWorks2008R2_Data.mdf ), `
`( FILENAME = ~/Desktop/data-engineering-assignment/database/AdventureWorks2008R2_log.LDF' ) `
`FOR ATTACH ;`
`GO`
