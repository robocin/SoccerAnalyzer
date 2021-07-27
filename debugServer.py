from flask.helpers import make_response
import pandas as pd
from flask import Flask
from flask_cors import CORS
import json
from common.basic.match import Match


################################## analysis setup ###############################
def analysis(match_object):
	# 1 - Análise/manipulação
	# aqui voce pode fazer alguma manipulação com os dados ( a análise em si). nesse caso não estou fazendo nenhuma análise, apenas passando ball_x da forma que a função recebeu.
	df = match_object.dataframe
	show_time =  list(df["show_time"])
	ball_x =  list(df["ball_x"])

	# 2 - Formatação
	# agora é só preparar os dados finais em um dicionário e retornar-los como uma string json
	resultDict = {
		"show_time" : show_time,
		"ball_x" : ball_x 
	}
	resultJson = json.dumps(resultDict)

	return resultJson 



################################## flask setup ###############################
# flask setup
app = Flask(__name__)
CORS(app)
# cors = CORS(app)
cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})

@app.route("/", methods=['GET'])
def hello_world():
	# reads .csv
	df = pd.read_csv('20200229162107-ThunderLeague_1-vs-RoboCIn_2.rcg.csv')	

	match_object = Match(df)

	# Chama a função de análise passando o match_object como argumento 
	result = analysis(match_object)

	# Retorna o resultado para quem pediu
	response = make_response(result)
	response.headers.add("Access-Control-Allow-Origin", "*")
	return result



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')