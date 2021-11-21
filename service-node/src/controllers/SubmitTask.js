'use strict';

var utils = require('../utils/writer.js');
var SubmitTask = require('../service/SubmitTaskService');

module.exports.createCase = function createCase (req, res, next, body) {
  SubmitTask.createCase(body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};
