SetupsModule.config(['$routeProvider', '$locationProvider', '$provide', function ($routeProvider, $locationProvider, $provide) {
    //$urlRouterProvider.otherwise('/tpl_recruitment');
    $routeProvider.when('/dashboard', {
            templateUrl: setupsTemplatePath + 'tpl_deshboard.html',
            controller: 'DashboardController'
        })
        .when('/basic_options', {
            templateUrl: setupsTemplatePath + 'tpl_basic_options.html',
            controller: 'BasicOptionsController'
        })
        .when('/setup_options', {
            templateUrl: setupsTemplatePath + 'tpl_setup_options.html',
            controller: 'ApplicantScoreController'
        })
        .otherwise({
            redirectTo: '/dashboard'
        });

    // $locationProvider.html5Mode({
    //     enabled: true,
    //     requireBase: false
    // });

    $locationProvider.html5Mode(true);
    // $provide.decorator('$sniffer', function ($delegate) {
    //     $delegate.history = false;
    //     return $delegate;
    // });
}]);
