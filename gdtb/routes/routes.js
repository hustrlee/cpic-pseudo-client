(function() {
    var serviceRoute;
    serviceRoute = require('../api/service/route');

    module.exports = function(app) {
        app.use('/api', serviceRoute);

    };

}).call(this);