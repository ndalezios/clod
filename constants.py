# MongoDB connection info
# Set this according to your Mongo server information
# Default is localhost
MONGODB_CONN = "mongodb://localhost:27017/"



# CADF event record map
EVENT_TYPE = '\"event_type"'
TIMESTAMP = "timestamp"
PAYLOAD = "payload"
PRIORITY = "priority"
PUBLISHER_ID = "publisher_id"
MESSAGE_ID = "message_id"

# depending on the event logging producing plattform,
# event's head field may vary...
# In this case we take all 4 cases regarding the white spaces around ":"
# removing whitespaces from string is not an option
START_KEY1 = '{"typeURI": "http://schemas.dmtf.org/cloud/audit/1.0/event"'
START_KEY2 = '{"typeURI" :"http://schemas.dmtf.org/cloud/audit/1.0/event"'
START_KEY3 = '{"typeURI" : "http://schemas.dmtf.org/cloud/audit/1.0/event"'
START_KEY4 = '{"typeURI":"http://schemas.dmtf.org/cloud/audit/1.0/event"'

SEPARATOR = "=============================================================="

BIG_DOC = """
  _____________________________________________________________________
 |_Ws'________|_mandatory_________________|_optional___________________|
 |What        | event.action              | event.reason               |
 |            | event.outcome             |                            |
 |            | event.eventType           |                            |
 |____________|___________________________|____________________________|
 |When        | event.eventTime           | reporter.timestamp         |
 |            |                           | event.duration             |
 |____________|___________________________|____________________________|
 |Who         | initiator.id              | initiator.credential       |
 |            | initiator.type            |                            |
 |____________|___________________________|____________________________|
 |FromWhere   |                           | initiator.addresses        |
 |            |                           | initiator.host             |
 |            |                           | initiator.geolocation      |
 |____________|___________________________|____________________________|
 |OnWhat      | target.id                 |                            |
 |            | target.type               |                            |
 |____________|___________________________|____________________________|
 |Where       | observer.id               | reporterstep.role          |
 |            | observer.type             | reporterster.reporterTime  |
 |____________|___________________________|____________________________|
 |ToWhere     |                           | target.addresses           |
 |            |                           | target.host                |
 |            |                           | target.geolocation         |
 |____________|___________________________|____________________________|
"""
