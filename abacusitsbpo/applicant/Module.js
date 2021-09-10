var DashboardHelper = {
	showLoader: function() {
		AppCore.loader.show({text: 'Working'});
	},
	hideLoader: function() {
		AppCore.loader.hide();
	},
	isEmptyObjMem: function(mem) {
		if (angular.isUndefined(mem) || !mem || mem == null || mem == '') {
			return true;
		}
		return false;
	}
};
var LoginLocation = '';
// $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken
var ApplicantModule = angular.module('Applicant', ['ngRoute', 'ngAnimate', 'ngResource', 'ngMessages', 'ui.bootstrap', 'ui.select', 'angularFileUpload', 'ngSanitize', 'ngCookies', 'ui.mask']).run( function run( $http, $cookies ){
    // For CSRF token compatibility with Django
    $http.defaults.headers.post['X-CSRFToken'] = $cookies.get('csrftoken');
});
ApplicantModule.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);