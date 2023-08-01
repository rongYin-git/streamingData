# streamingData

This repo contains codes that can perform the following: 

streaming data from an open source weather API -> transform data -> use Kafka to process the streaming data -> post data to Power BI dashboard

Here are the steps for how to use the material in this repo.

Step 1: start Kafka in the terminal

\# start zookeeper

`bin/zookeeper-server-start.sh config/zookeeper.properties`

\# start kafka
`bin/kafka-server-start.sh config/server.properties`


