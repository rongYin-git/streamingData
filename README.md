# streamingData

This repo contains codes that can perform the following: 

streaming data from an open source weather API -> transform data -> use Kafka to process the streaming data -> post data to Power BI dashboard

Here are the steps for how to use the material in this repo.

Step 1: start Kafka via CLI

\# start zookeeper

`bin/zookeeper-server-start.sh config/zookeeper.properties`

\# start kafka

`bin/kafka-server-start.sh config/server.properties`

Step 2: run `setup_kafka.py`

This script creates new topics.

Step 3: run the `kafka_dashboard.py` script 

This script can stream data, transform data, publish/consume data using kafka and send data to dashboard 

You need to set up the following values before running the script:

- cur_url = #"REPLACE THIS STRING with your own API to retrieve current weather data"
- ago24h_url = #"REPLACE THIS STRING with your own API to retrieve weather data from 24 hours ago"
- endpoint = #"REPLACE THIS STRING with your own API for powerBI"






