import click, http.client, json

locations = {
	"Rift Valley": 400744,
	"Nyanza": 182763,
	"Coast" : 400740,
	"Western": 400743,
	"Central": 400742,
	"Nairobi": 184742,
	"Eastern": 400741,
	"North Eastern": 400745
}


def RequestOpenWeather(code):
	conn = http.client.HTTPConnection("api.openweathermap.org", 80)
	conn.request("GET", "/data/2.5/weather?id="+str(code)+"&appid=071be05bfba2c97dd5e60e061664c889")
	response = conn.getresponse()
	click.echo('Request State: '+str(response.status)+' - '+response.reason)
	data = json.loads(response.read().decode("UTF-8"))
	click.echo("Description: "+data['weather'][0]['description']+"\nTemperature: "+str(data['main']['temp'])+" Kelvin")

def ShowProvnices():
	for i in locations.keys():
		click.echo(i)

def CleanInput(inp):
	if type(inp) is str:
		inp = inp.strip()
		inp = inp.lower()
		inp = inp.title()
		if inp in locations:
			#to do
			click.echo("Incoming Information ....")
			RequestOpenWeather(locations[inp])
			#click.echo(info)
		else:
			click.echo("Please try again providing your selected province as specified")
	else:
		click.echo("Please try again providing your selected province as specified")

@click.command(ShowProvnices())
@click.option('--province', prompt="Please enter the province you would like the weather for",
              help='The province in Kenya you would like to know the weather for.')
def  KenyanWeather(province):
    """Simple program that request weather information based on select provinces in Kenya."""
    CleanInput(province)

if __name__ == '__main__':
    KenyanWeather()

