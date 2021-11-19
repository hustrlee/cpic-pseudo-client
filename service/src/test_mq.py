from cpic_interface.mq_config import CasePublisher

mq = CasePublisher()

for i in range(500):
    mq.connect()
    mq.publish("from medical_review exchange!")
    mq.close()
