//var ApplicantRouter = angular.module('DashboardRouter', ['ngRoute', 'ngAnimate', 'ApplicantModule', 'DashboardService', 'ui.bootstrap']);//, 'SharedServices','AdminFilter', 'AppDirective', 'AppFilter'
//var UsersRouter = angular.module('UsersRouter', ['ngRoute', 'UsersControllers', 'UsersService']);
ApplicantModule.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
	$routeProvider								
	.when('/' , {templateUrl: 'static/applicant/tpl_applicants.html', controller: 'ApplicantController'})
	.otherwise({redirectTo: '/'});
	//.otherwise({redirectTo: '/'}); 
	$locationProvider.html5Mode(true);
	/*$locationProvider.html5Mode({
	  enabled: true,
	  requireBase: false
	});*/
}]);
