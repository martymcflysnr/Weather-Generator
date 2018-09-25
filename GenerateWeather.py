import os
import matplotlib.image as mpimg
import random
import decimal
import datetime as dt
import pandas as pd


def generate_weather():
	# Initialise reference data dir and file names
	elevation_file_name = 'elevation_JB.BMP'
	city_file_name = 'world_capitals_lat_long.csv'
	reference_data_dir = 'reference_data'
	
	# Check expected directory and files exist
	if not os.path.exists(os.path.join(os.getcwd(),reference_data_dir)):
		print (os.path.join(os.getcwd(),reference_data_dir)+' does not exist! Please create it copy the required files.')
		exit(1)
		
	if not os.path.exists(os.path.join(os.getcwd(),reference_data_dir,elevation_file_name)):
		print (os.path.join(os.getcwd(),reference_data_dir,elevation_file_name)+' does not exist! Please put the file in this location.')
		exit(1)

	if not os.path.exists(os.path.join(os.getcwd(),reference_data_dir,city_file_name)):
		print (os.path.join(os.getcwd(),reference_data_dir,city_file_name)+' does not exist! Please put the file in this location.')
		exit(1)	
		
	# Get the source data file paths
	elevation_img_file = os.path.join(os.getcwd(),reference_data_dir,elevation_file_name)
	city_lat_long_file = os.path.join(os.getcwd(),reference_data_dir,city_file_name)

	# Read the elevation image file into a 3D Numpy array
	img = mpimg.imread(elevation_img_file)

	# Read the city latitude/longitude file and store into a dataframe
	city_file = pd.read_csv(city_lat_long_file, sep=',')
	
	# Get a random list of cities
	city_list = random.sample(range(city_file.shape[0]), 20)
	
	# Get the dimensions of the image file for later use
	elevation_img_height = int(img.shape[0])
	elevation_img_width = int(img.shape[1])
	
	for c in city_list:
		# Get the formatted latitude/longitude and x/y co-ordinates for our elevation image
		output_lat, output_long, x, y = lat_long_coords(city_file.iloc[c,2],city_file.iloc[c,3],elevation_img_height,elevation_img_width)
		
		# Get elevation using x and y co-ordinates - 0 for Red channel
		output_elevation = str(img[x,y,0])
		
		# Generate random time
		output_time = str(random_date_time())
		
		# Generate random conditions
		output_conditions = random_weather_conditions()

		# Generate random temperature
		output_temperature = str(format(decimal.Decimal(random.randrange(-100, 401))/10,'+'))
	
		# Generate random pressure
		output_pressure = str(decimal.Decimal(random.randrange(8700, 10858))/10)
	
		# Generate random humidity
		output_humidity = str(random.choice(range(0,101)))
		
		# Print city geography details including fake weather
		print(str(city_file.iloc[c,1])+'|'+str(output_lat)+','+str(output_long)+','+output_elevation+'|'+output_time+'|'+output_conditions+'|'+output_temperature+'|'+output_pressure+'|'+output_humidity)

# Function to format latitude/longitude and return x/y co-ordinates of that position on the image
def lat_long_coords( latitude, longitude, img_x, img_y):
	
	if latitude.endswith('S'):
		# Negate the latitude value South of the equator and remove 'S'
		latitude_formatted = float((latitude[:-1]))*-1
		# Calculate the x co-ordinate for this latitude
		x_coord = ((abs(latitude_formatted)/90*img_x/2)+(img_x/2)-1)
	elif latitude.endswith('N'):
		# Remove the 'N' from the latitude
		latitude_formatted = float(latitude[:-1])
		# Calculate the x co-ordinate for this latitude
		x_coord = ((img_x/2)-(abs(latitude_formatted)/90*img_x/2))	
		
	if longitude.endswith('W'):
		# Negate the latitude value West of the Prime Meridian and remove 'W'
		longitude_formatted = float(longitude[:-1])*-1
		# Calculate the y co-ordinate for this longitude
		y_coord = ((img_y/2)-(abs(longitude_formatted)/180*img_x/2))
	elif longitude.endswith('E'):
		# Remove the 'E' from the latitude
		longitude_formatted = float(longitude[:-1])
		# Calculate the y co-ordinate for this latitude
		y_coord = ((abs(longitude_formatted)/180*img_y/2)+(img_y/2)-1)

	
	return latitude_formatted, longitude_formatted, int(round(x_coord,0)), int(round(y_coord,0))

# Function to generate a random date_time in ISO8601 format
def random_date_time ():
	
	# Generate random year and month
	year = str(random.choice(range(1980, dt.datetime.now().year)))
	month = str(random.choice(range(1, 13)))

	# Generate date based on month and if it's a leap year if the month is February
	months_31day = frozenset([1,3,5,7,8,10,12])
	# 31 day month
	if int(month) in months_31day:
		day = str(random.choice(range(1, 32)))
	# February
	elif int(month) == 2:
		# 29 day February
		if int(year) % 4 == 0:
			day = str(random.choice(range(1, 30)))
		# Otherwise 28 day February
		else:
			day = str(random.choice(range(1, 29)))
	# 30 day month
	else:
		day = str(random.choice(range(1, 31)))

	# Generate random time components
	hour = str(random.choice(range(0,24)))
	minute = str(random.choice(range(0,60)))
	second = str(random.choice(range(0,60)))
	
	#Construct date_time from generated random values
	date_time = dt.datetime.strptime(year+'-'+month.zfill(2)+'-'+day.zfill(2)+hour+':'+minute+':'+second, "%Y-%m-%d%H:%M:%S").replace(microsecond=0).isoformat()
	
	# Return date_time in ISO8601 format
	return str(date_time)+'Z'

def random_weather_conditions ():
	weather_conditions = ['Snow','Rain','Sunny']
	return random.choice(weather_conditions)
 
generate_weather()




	
	