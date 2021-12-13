'use strict'

/*
|--------------------------------------------------------------------------
| Routes
|--------------------------------------------------------------------------
|
| Http routes are entry points to your web application. You can create
| routes for different URL's and bind Controller actions to them.
|
| A complete guide on routing is available here.
| http://adonisjs.com/docs/4.1/routing
|
*/

/** @type {typeof import('@adonisjs/framework/src/Route/Manager')} */
const Route = use('Route')

Route.post("/writeMetric", 'ResourceController.writeMetric')

Route.get("/getMetric", 'ResourceController.getMetric')

Route.post("/writeTempValue", 'ResourceController.writeTempValue')

Route.get("/getTempValue", 'ResourceController.getTempValue')

Route.get("/getIdAndMetric", 'ResourceController.getIdAndMetric')

Route.get("/getPodList", 'ResourceController.getPodList')

Route.get("/healthz", 'ResourceController.checkHealth')

//Route.get('/writeMetric/:value', 'ResourceController.writeQueryMetric')

Route.get('/writeMetric', 'ResourceController.writeQueryMetric')

Route.get('/register', 'ResourceController.register')
