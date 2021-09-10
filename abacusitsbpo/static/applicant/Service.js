//var svcRouter = angular.module('DashboardService', ['ngResource']);
//var svcRouter = angular.module('UsersService', ['ngResource']);
ApplicantModule.factory('ApplicantServices', ['$resource', function($resource) {
    //console.log(servicesPath);
	return $resource(':action');
}]);
/*svcRouter.factory('SvcUsers', ['$resource', function($resource) {
	var params = {
		token: token
	};
	return $resource(servicesPath+'/:action', params);
}]);*/

