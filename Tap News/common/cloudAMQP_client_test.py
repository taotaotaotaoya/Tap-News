from cloudAMQP_client import CloudAMQPClient

TEST_CLOUDAMQP_URL = #TODO: use your own config.
TEST_QUEUE_NAME = #TODO: use your own config.

def test_basic():
    client = CloudAMQPClient(TEST_CLOUDAMQP_URL, TEST_QUEUE_NAME)

    sentMsg = {'test':'test'}
    client.sendMessage(sentMsg)

    client.sleep(5)

    receivedMsg = client.getMessage()
    assert sentMsg == receivedMsg

    print('test_basic passed.')

if __name__ == "__main__":
    test_basic()
