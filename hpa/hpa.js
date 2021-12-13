require('dotenv').config()
const axios = require('axios');
const exec = require('child_process').exec;
const CronJob = require('cron').CronJob;

const args = {}
const METRICS_URL = process.env.METRICSSERVER_URL;
var currentReplicas = 1;
const reactionTime = 50; //tempo de reação em segundos
var lastReactionTime = new Date().getTime();
var first = true;

function parseArgs(){
    const flags = process.argv.slice(2);

    flags.map(item => {
        let command = item.split("=")

        args[command[0]] = command[1]; 
    })

}

parseArgs();

if(!args.metricThreshold){
    console.log("É necessário informar o metricThreshold");
    return -1;
}

const metricThreshold = args.metricThreshold;

var job = new CronJob(`*/${args.getMetricTime || 5} * * * * *`, function() {
    console.log("Coletando métricas...");
    axios.get(`http://34.132.43.90:3333/getMetric`)
    .then(res => {
        const {media, qtdReq} = res.data;
        if(media == -1){
            console.log("Não há eventos a serem coletados.")
        } else {
            console.log(`Valor coletado: { value: ${media}, qtdReq: ${qtdReq} }`);
            if (!first && ((new Date().getTime() - lastReactionTime)/1000 < reactionTime)){
                console.log(`Ainda não é possivel reagir.`);
            } else {
                var desiredReplicas = Math.ceil((currentReplicas * ( media / metricThreshold)));

                if(desiredReplicas > currentReplicas){
                    lastReactionTime = new Date().getTime();
                    first = false;
                    if(desiredReplicas > currentReplicas){
                        console.log(`Adicionando ${desiredReplicas - currentReplicas} réplicas.`);
                    } /*else if (desiredReplicas < currentReplicas){
                        console.log(`Removendo ${currentReplicas - desiredReplicas} réplicas.`);
                    }*/
    
                    exec(`kubectl scale deployments/interscity-hpa-deployment --replicas=${desiredReplicas}`, function (error, stdOut, stdErr) {});
                    currentReplicas = desiredReplicas;
                }
                //if(media > metricThreshold){
                    /*switch(currentReplicas){
                        case 1:
                            console.log("Adicionando nova réplica");
                            exec(`kubectl scale deployments/interscity-hpa-deployment --replicas=2`, function (error, stdOut, stdErr) {});
                            currentReplicas = 2;
                            lastReactionTime = new Date().getTime();
                        break;
                        case 2:
                            console.log("Adicionando 3 novas réplicas");
                            exec(`kubectl scale deployments/interscity-hpa-deployment --replicas=5`, function (error, stdOut, stdErr) {});
                            currentReplicas = 5;
                            lastReactionTime = new Date().getTime();
                        break;
                        case 5:
                            console.log("Limite de replicas alcançado");
                        break;
                    }*/
                //}
            }
            
            /*if(desiredReplicas == 0) desiredReplicas = 1;
            if(desiredReplicas > 3) desiredReplicas = 3;

            console.log(`A quantidade de réplicas calculada foi ${desiredReplicas}`);
            console.log(`A quantidade atual de réplicas é ${currentReplicas}`)
            
            if(currentReplicas != desiredReplicas){
                if ((new Date().getTime() - lastReactionTime)/1000 < reactionTime){
                    console.log(`Ainda não é possivel reagir.`);
                } else {
                    lastReactionTime = new Date().getTime();
                    if(desiredReplicas > currentReplicas){
                        console.log(`Adicionando ${desiredReplicas - currentReplicas} réplicas.`);
                    } else if (desiredReplicas < currentReplicas){
                        console.log(`Removendo ${currentReplicas - desiredReplicas} réplicas.`);
                    }
    
                    exec(`kubectl scale deployments/interscity-hpa-deployment --replicas=${desiredReplicas}`, function (error, stdOut, stdErr) {});
                    currentReplicas = desiredReplicas;
                }
            } else {
                console.log(`Não é necessário criar/remover nenhuma réplica.`);
            }*/
        }
    })
    .catch(error => {
        console.log("ERROR >>", error)
    })
}, null, true, 'America/Los_Angeles');

job.start();

