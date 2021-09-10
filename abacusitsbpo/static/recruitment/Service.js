RecruitmentModule.factory('Svc', ['$resource', function($resource) {
	var params = {
		token: token
	};
	return $resource(recruitmentServicesPath+'/:action', params);
}]);
/*svcRouter.factory('SvcUsers', ['$resource', function($resource) {
	var params = {
		token: token
	};
	return $resource(servicesPath+'/:action', params);
}]);*/

