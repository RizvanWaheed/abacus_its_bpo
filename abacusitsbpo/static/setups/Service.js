SetupsModule.factory('Svc', ['$resource', function($resource) {
	var params = {
		token: token
	};
	return $resource(setupsServicesPath+'/:action', params);
}]);
/*svcRouter.factory('SvcUsers', ['$resource', function($resource) {
	var params = {
		token: token
	};
	return $resource(servicesPath+'/:action', params);
}]);*/

