



from flask import Flask , render_template , request

import json 




app = Flask(__name__)




with open('groups.json') as f :
  data = json.load(f)



datalist = data['data']['list']


deep_similar_groups = {}

for x in datalist:
  deep_similar_groups[ x['categories'][0]['main_category_name'] + " + "  + x['categories'][0]['category_name'] ] = []



for x in datalist : 
  deep_similar_groups[ x['categories'][0]['main_category_name'] + " + "  + x['categories'][0]['category_name'] ].append(x)



output_similar_group_ids= {}

for x in datalist:
    output_similar_group_ids[x['group_id']] = []





for x in deep_similar_groups:
  for y in deep_similar_groups[x]:
    t = y['group_id']
    for z in deep_similar_groups[x]:
      output_similar_group_ids[t].append(z['group_id'])



@app.route('/')
def main():
    return render_template('main.html')

@app.route('/data' , methods = ['POST'])
def func():
    form_data = request.form['Name']
    returndata = output_similar_group_ids[form_data]
    
    return render_template('data.html' , returndata = returndata)
    









