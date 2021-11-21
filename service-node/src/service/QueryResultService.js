'use strict';


/**
 * 查询任务状态，及识别结果
 *
 * body QueryCaseDto  (optional)
 * returns QueryCaseResDto
 **/
exports.queryCase = function(body) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = {
  "msg" : "msg",
  "code" : 0,
  "data" : {
    "result" : [ {
      "imageId" : "imageId",
      "imageName" : "imageName",
      "moreThanOneList" : 5.637376656633329,
      "details3" : [ "", "" ],
      "details2" : [ "", "" ],
      "details4" : [ "", "" ],
      "remark" : "remark",
      "details1" : [ "", "" ]
    }, {
      "imageId" : "imageId",
      "imageName" : "imageName",
      "moreThanOneList" : 5.637376656633329,
      "details3" : [ "", "" ],
      "details2" : [ "", "" ],
      "details4" : [ "", "" ],
      "remark" : "remark",
      "details1" : [ "", "" ]
    } ],
    "caseState" : {
      "ymark" : "ymark",
      "state" : 6,
      "uploadTime" : "uploadTime",
      "zmark" : "zmark"
    },
    "caseInfo" : {
      "invoiceList" : [ "", "" ],
      "insureName" : "insureName",
      "admissionDate" : "admissionDate",
      "dischargeDate" : "dischargeDate",
      "costType" : "门诊",
      "hospitalizationDays" : 5.962133916683182,
      "insurecode" : "insurecode",
      "registNo" : "registNo",
      "invoiceTotalAmount" : 1.4658129805029452,
      "caseNo" : "caseNo"
    }
  },
  "uuid" : "uuid"
};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}

