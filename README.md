# Detection of Blighted Houses in Detroit
By Kwang Ho Hur

## Issue and Motivation
* Blighted houses or buildings are problematic in a lot of cities because of
	- Threat to public safety
	- More blighted houses can be created in the neighborhood. 
	- Concern for real estate
* This issue has been much more serious in Detroit because of the enormous decline of its population during the last 60 years. In the city, lots of houses have been abandoned. This enables me to build a classification model where the number of blighted houses is high enough to be detectable. Otherwise, we need develop an anomaly detection model. 

## Solution
1. Build a classification model which can identify blighted houses in the city.
2. Evaluate the accuracy of the model 
3. Develop a method employing images 

## Data
* Phase 1
  Using public data from Detroit
	- Demolition Permits
	- Blight Violation Tickets
	- Crimes
	- 311 Calls

## Workflow
* Perform feature engineering to build a sructured data from four sets of data.
* Build a classification model with a metric precision.

## Steps
1. **Using Public Data**
	- [x] Identify blighted houses/buildings from Demolition Permits (pandas in Python)
	      : address, latitude, and longitude
	- [x] Identify unblighted houses/buildings from Blight Violation Tickets (pandas in Python) 
	      : address, latitude, and longitude
	- [x] Assign the number of blight violation tickets, the number of crimes, and the number of 311 calls 
		  to blighted/non-blighted houses/buildings (numpy in Python)
	- [x] Build a K-Nearest Neighbor Classification model.
	- [ ] Consider ViolationCode, Disposition, and PaymentStatus in Blight Violation Tickets.
	- [ ] Consider Category, Precinct in Crimes
	- [ ] Consider Issue_type, Rating in 311 Calls

2. Using images
	- [ ] Collect images of blighted houses/buildings
	- [ ] Collect images of non-blighted houses/buildings