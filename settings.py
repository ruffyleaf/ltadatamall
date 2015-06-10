"""
In this file, you should enter all credentials for use for data extraction
ACCOUNT_KEY is given my the API service.

UNIQUE_USER_ID needs to be obtained by providing your ACCOUNT_KEY to http://datamall.mytransport.sg/tool.aspx

The other fields are used to store the URLs of the web APIs
"""

ACCOUNT_KEY = 'uCqGQQQuptMQrt7yLT4GUg=='

UNIQUE_USER_ID = '2015a2e7-3a6b-45a2-a07c-b1271f0fc178'

#Public Transport Related URL

#Take note for Bus Arrival, the BusStopID is a mandatory field to pass into the URL
BUS_ARRIVAL = 'http://datamall2.mytransport.sg/ltaodataservice/BusArrival'

SBS_BUS_ROUTE = 'http://datamall.mytransport.sg/ltaodataservice.svc/SBSTRouteSet'
SBS_BUS_INFO = 'http://datamall.mytransport.sg/ltaodataservice.svc/SBSTInfoSet'

SMRT_BUS_ROUTE = 'http://datamall.mytransport.sg/ltaodataservice.svc/SMRTRouteSet'
SMRT_BUS_INFO = 'http://datamall.mytransport.sg/ltaodataservice.svc/SMRTInfoSet'

BUS_STOPS = 'http://datamall.mytransport.sg/ltaodataservice.svc/BusStopCodeSet'

TAXI_AVAIL = 'http://datamall2.mytransport.sg/ltaodataservice/TaxiAvailability'

#Traffic Related
CARPARK_AVAIL = 'http://datamall.mytransport.sg/ltaodataservice.svc/CarParkSet'

ERP_RATES = 'http://datamall.mytransport.sg/ltaodataservice.svc/ERPRateSet'

EST_TRAVEL = 'http://datamall.mytransport.sg/ltaodataservice.svc/TravelTimeSet'

FAULTY_TRAFFIC_LIGHTS = 'http://datamall.mytransport.sg/ltaodataservice.svc/AlarmInfoSet'

ROAD_OPENINGS = 'http://datamall.mytransport.sg/ltaodataservice.svc/PlannedRoadOpeningSet'

ROAD_WORKS = 'http://datamall.mytransport.sg/ltaodataservice.svc/RoadWorkSet'

TRAFFIC_IMAGES = 'http://datamall.mytransport.sg/ltaodataservice.svc/CameraImageSet'

TRAFFIC_INCIDENTS = 'http://datamall.mytransport.sg/ltaodataservice.svc/IncidentSet'

SPEED_BANDS = 'http://datamall.mytransport.sg/ltaodataservice.svc/TrafficSpeedBandSet'

VMS_EMAS = 'http://datamall.mytransport.sg/ltaodataservice.svc/VMSSet'
