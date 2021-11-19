from cpic_interface.mq_config import mq

mq.create()

mq.publish("from medical_review exchange!")

mq.close()
