'use strict'

const { v4: uuidv4 } = require('uuid');
const initTime = Date.now();
var events = {};
var reqAtendidas = {}
const sum = {};
const defaultValues = {
    default: 50
}
var collectedData = {}
const hpaList = [];
const podList = [];

class ResourceController {
    async getMetric({request}){
        console.log("=======GetMetric=======");
        console.log(collectedData)
        const {value, qtd, eventos} = collectedData;

        if(!qtd || qtd == 0){
            console.log("Não há metricas para serem enviadas.")
            return {media: 0, qtdReq: 0};
        }

        const media = value/eventos;
        collectedData = {};

        console.log("Media: ", media);
        console.log("=======================");

        return {media, qtdReq: qtd};
        // console.log("URL: ", METRICS_URL)

        // axios.get(`${METRICS_URL}/writeMetric/${parseInt(media)}`)
        // .then(res => {
        //     console.log("Métrica enviada.")
        // })
        // .catch(error => {
        //     console.log("Erro ao enviar métrica >>", error)
        // })
    }

    async writeMetric ({request}){

        console.log("======WriteMetric======");
        const data = request.post();
        const metricName = data.metricName? data.metricName : 'processTime';

        console.log(`Valor recebido > ${metricName}: ${data.value}`);
        if(!data.value){
            console.log("=======================");
            return -1;
        }

        const value = data.value;

        events[metricName] = events[metricName]? events[metricName] + 1 : 1;
        sum[metricName] = sum[metricName]?  sum[metricName] + parseFloat(value) : parseFloat(value);

        console.log("=======================");
        return 1;
    }

    async register ({params}){
      console.log("========REGISTER========");
      var uuid = uuidv4();

      hpaList.push(uuid);
      return uuid;
    }

    async writeQueryMetric({request, response}){
        console.log("======WriteMetric======");
        const queryData = request.get();

        if(!queryData.value || !queryData.qtd){
          console.log("Faltam dados na requisição >>", queryData)
          return response.status(400).send("Os parâmetros id e value são obrigatórios.");
        }

        if(!queryData.value || queryData.value == '0') queryData.qtd = 0;

        console.log(`Value: ${queryData.value}`);
        console.log(`Qtd: ${queryData.qtd}`);
        const {value, qtd} = queryData;

        if(collectedData.value == undefined){
          collectedData.value = parseFloat(value)
          collectedData.qtd = parseInt(qtd)
          collectedData.eventos = 1
        } else {
            collectedData.value = collectedData.value + parseFloat(value)
            collectedData.qtd = collectedData.qtd + parseInt(qtd)
            collectedData.eventos = collectedData.eventos + 1
        }
    }

    async getTempValue({request}){
        const data = request.get();
        const podID = data.podID? data.podID : 'default';

        if(!podList.some(item => item == podID)){
            podList.push(podID);
        }

        if(defaultValues[podID]){
            return defaultValues[podID];
        }

        return defaultValues.default;
    }

    async getPodList({request}){
        return podList;
    }

    async getIdAndMetric({request}){
        return collectedData;
    }

    async writeTempValue({request}){
        const data = request.post();
        const {podID, value} = data;

        defaultValues[podID] = value;

        return value;
    }

    async checkHealth({response}){
        const env = process.env;
        let seconds = (Date.now() - initTime)/1000;
        if(seconds > env.READINESS_TIME){
            response.status(200).send(seconds);

        } else {
            response.status(400).send(seconds);
        }
    }
}

module.exports = ResourceController
