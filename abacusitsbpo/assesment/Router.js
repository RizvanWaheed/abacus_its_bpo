AssesmentModule.config(['$routeProvider', '$locationProvider', '$provide', function ($routeProvider, $locationProvider, $provide) {
    //$urlRouterProvider.otherwise('/tpl_recruitment');
    $routeProvider.when('/dashboard', {
            templateUrl: assesmentTemplatePath + 'tpl_deshboard.html',
            controller: 'DashboardController'
        })
        .when('/new_assesment', {
            templateUrl: assesmentTemplatePath + 'tpl_assesment_form.html',
            controller: 'AssesmentController'
        })
        .when('/applicant_score', {
            templateUrl: assesmentTemplatePath + 'tpl_applicant_score.html',
            controller: 'ApplicantScoreController'
        })
        .otherwise({
            redirectTo: '/'
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
