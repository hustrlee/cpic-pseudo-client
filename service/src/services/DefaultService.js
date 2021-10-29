/* eslint-disable no-unused-vars */
const Service = require('./Service');

/**
* 用于接收渠道推送的案件信息
*
* createCaseDto CreateCaseDto 
* returns ResDto
* */
const createCasePOST = ({ createCaseDto }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        createCaseDto,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);

module.exports = {
  createCasePOST,
};
