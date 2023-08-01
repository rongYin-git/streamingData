from kafka.admin import NewTopic, KafkaAdminClient, ConfigResource, ConfigResourceType

if __name__ == "__main__":
    
    ##start terminal
    #bin/zookeeper-server-start.sh config/zookeeper.properties
    #bin/kafka-server-start.sh config/server.properties
    
    ##set up kafka
    #admin
    admin_client = KafkaAdminClient(
        bootstrap_servers="localhost:9092", 
        client_id='test'
    )

    #new topic - only need to set up once
    topic_list = []

    topic_current = NewTopic(name="current", num_partitions= 1, replication_factor=1)
    topic_24hAgo = NewTopic(name="24hAgo", num_partitions= 1, replication_factor=1)

    topic_list.extend([topic_current, topic_24hAgo])
    admin_client.create_topics(new_topics=topic_list, validate_only=False)

    print(f'The current topics are: {admin_client.list_topics()}')
    
    #check lags in terminal
    #bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group current
    #bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group 24hAgo
    
    