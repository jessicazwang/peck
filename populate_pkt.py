import csv
import os

def populate():
	with open('populate-pkt.csv','rb') as csvfile:
		reader = csv.reader(csvfile)

		for row in reader:
			try:
				name = row[0]
				year = row[1]
				photo = row[2]
				nickname = row[3]
				initials = row[4]
				hometown = row[5]
				major = row[6]
				activities = row[7]
				quote = row[8]
				blurb = row[9]
				add_brother(name,year,photo,nickname,initials,hometown,major,activities,quote,blurb)
			except:
				pass

def add_brother(name,year,photo,nickname,initials,hometown,major,activities,quote,blurb):
	b = Brother.objects.get_or_create(name=name,year=year,photo=photo,nickname=nickname,initials=initials,hometown=hometown,major=major,activities=activities,quote=quote,blurb=blurb)
	return b

if __name__=='__main__':
	print "Starting population script"
	os.environ.setdefault('DJANGO_SETTINGS_MODULE','pkt.settings')
	from website.models import Brother
	populate()