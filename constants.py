# CADF event record map
EVENT_TYPE = '\"event_type"'
TIMESTAMP = "timestamp"
PAYLOAD = "payload"
PRIORITY = "priority"
PUBLISHER_ID = "publisher_id"
MESSAGE_ID = "message_id"

START_KEY = "{" + EVENT_TYPE
START_CADF_KEY = """ {"typeURI": "http://schemas.dmtf.org/cloud/audit/1.0/event" """

END_KEY = "}"
