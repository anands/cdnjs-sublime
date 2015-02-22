import json
import re

def saveScript(repo):
	script = """
<snippet>
<content><![CDATA[
<script src="{0}"></script>
]]></content>	
	<tabTrigger>{1}</tabTrigger>
</snippet>
		  """
	data = script.format(repo['Link'], repo['Library'])
	f = open("snippets/"+repo['Library']+".js.sublime-snippet",'w')
	f.write(data)
	f.close() 
def saveStyle(repo):
	stylesheet = """
<snippet>
	<content><![CDATA[
<link href="{0}" rel="stylesheet">
]]></content>	
	<tabTrigger>{1}</tabTrigger>
</snippet>
			"""
	data = stylesheet.format(repo['Link'], repo['Library'])
	f = open("snippets/"+repo['Library']+".css.sublime-snippet",'w')
	f.write(data)
	f.close()

def init():
	json_data=open('cdnjs.json')
	cdnjs = json.load(json_data)
	for repo in cdnjs:	
		if(re.search(".js$",repo['Link'])):			
			saveScript(repo)
		if(re.search(".css$",repo['Link'])):
			saveStyle(repo)

init()