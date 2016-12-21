from bs4 import BeautifulSoup
import os
import urllib
from urllib import parse, request
import sys
import pickle
import json
if __name__ == "__main__":
	api_url = 'http://sweetcooking.me/api/ingredients?pagenum=1&size=2000'
	api_content = request.urlopen(api_url)
	api_dict = json.loads(str(api_content.read().decode('utf-8')))
	api_ingredients = api_dict['ingredients']
	recipe_count = {}
	for ingredient in api_ingredients:
		recipe_count['ingredient.' + ingredient['name']] = len(ingredient['recipes'])
	
	with open("api.csv", "w") as myfile:
		myfile.write("id,value\n")
		myfile.write("ingredient\n")
		for ingredient in recipe_count.keys():
			myfile.write(ingredient + ',' + str(recipe_count[ingredient]) + '\n')
	
	#print(recipe_count)