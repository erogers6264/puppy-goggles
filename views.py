from flask import 

@app.route('/')
@app.route('/shelters/')
def puppyShelters():
	return "This page will show all the shelters"

@app.route('/shelters/<int:shelter_id>/')
def puppies(shelter_id):
	return "This page will list puppies in a shelter"