'use strict';

var utils = require('../utils/writer.js');
var QueryResult = require('../service/QueryResultService');

module.exports.queryCase = function queryCase (req, res, next, body) {
  QueryResult.queryCase(body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};
