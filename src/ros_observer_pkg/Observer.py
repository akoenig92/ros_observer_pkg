import rospy
import time


# ----------------------------------------------------------------------------------------------------------------------
# Maintains subscribers to all the given topics
# checks for remaps by itself
# gets message type by itself
# get get the current values via get_message
class Observer:

    def __init__(self, topics, event=None):

        # ----------------------------------------------------------------------
        # initialize dictionaries
        self.topic_mappings = self.create_remap_dictionary(topics)

        # -----
        # Set threading event to signal that the node is now waiting for topics to come up
        if event:
            event.set()
        # -----

        self.topics_and_types = self.create_topic_dictionary(topics, self.topic_mappings)
        self.observed_topics = {}
        self.update_times = {}

        rospy.loginfo("Start Observer")
        rospy.loginfo("Wait for necessary topics")

        for t in self.topics_and_types:
            self.update_times[t] = time.time()

        # ----------------------------------------------------------------------
        # Import necessary message types and wait for messages to be published
        for t in self.topics_and_types:
            exec("from {}.msg import {}".format(self.topics_and_types[t][0], self.topics_and_types[t][1]))
            rospy.wait_for_message(self.topic_mappings[t],
                                   eval(self.topics_and_types[t][1]))

        # ----------------------------------------------------------------------
        # Initialize subscriber
        subs = {}
        for t in self.topics_and_types:
            subs[t] = rospy.Subscriber(self.topic_mappings[t],
                                       eval(self.topics_and_types[t][1]),
                                       self.observe,
                                       t,
                                       queue_size=1)
        rospy.loginfo("Take 1 second to start subscriber")
        time.sleep(1)

        for s in subs:
            rospy.loginfo("Observer subscribes to {}".format(subs[s].name))

    # --------------------------------------------------------------------------
    # Stores the received message
    def observe(self, data, topic):
        self.observed_topics[topic] = data
        self.update_times[topic] = time.time()

    # --------------------------------------------------------------------------
    # Getter method for the messages of a given topic
    def get_message(self, topic):
        return self.observed_topics[topic]

    # --------------------------------------------------------------------------
    # Getter method for the last update time delay of a given topic
    def get_update_time(self, topic):
        return self.update_times[topic]

    # --------------------------------------------------------------------------
    # Gets message types for each topic
    @staticmethod
    def create_topic_dictionary(topics, topic_mappings):

        rospy.loginfo("Waiting for topics to come up")
        while True:
            types = [t for t in rospy.get_published_topics() if t[0] in topic_mappings.values()]
            if len(types) == len(topics):
                break

        reversed_mappings = {value: key for key, value in topic_mappings.items()}

        types = [(reversed_mappings[t[0]], t[1]) for t in types]

        result = {}
        for t in types:
            result[t[0]] = [str(s) for s in t[1].split("/")]
        return result

    # --------------------------------------------------------------------------
    # Gets mappings for each topic
    @staticmethod
    def create_remap_dictionary(topics):
        mappings = rospy.names.get_mappings()
        result = {}
        for t in topics:
            result[t] = t if t not in mappings else mappings[t]
        return result
