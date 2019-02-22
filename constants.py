# CADF event record map
EVENT_TYPE = '\"event_type"'
TIMESTAMP = "timestamp"
PAYLOAD = "payload"
PRIORITY = "priority"
PUBLISHER_ID = "publisher_id"
MESSAGE_ID = "message_id"

START_KEY = "{" + EVENT_TYPE
START_CADF_KEY = """ {"typeURI":" http://schemas.dmtf.org/cloud/audit/1.0/event" """

END_KEY = "}"

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
