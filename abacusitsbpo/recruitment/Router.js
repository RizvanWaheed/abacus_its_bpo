RecruitmentModule.config(['$routeProvider', '$locationProvider', '$provide', function ($routeProvider, $locationProvider, $provide) {
    //$urlRouterProvider.otherwise('/tpl_recruitment');
    $routeProvider.when('/dashboard', {
            templateUrl: recruitmentTemplatePath + 'tpl_deshboard.html',
            controller: 'DashboardController'
        })
        .when('/', {
            templateUrl: recruitmentTemplatePath + 'tpl_deshboard.html',
            controller: 'DashboardController'
        })
        .when('/recruitment', {
            templateUrl: recruitmentTemplatePath + 'tpl_recruitment.html',
            controller: 'RecruitmentController'
        })
        .when('/recruitment_report', {
            templateUrl: recruitmentTemplatePath + 'tpl_recruitment_report.html',
            controller: 'RecruitmentReportController'
        })
        .when('/interview_approval', {
            templateUrl: recruitmentTemplatePath + 'tpl_interview_approval.html',
            controller: 'InterviewApprovalController'
        })
        .when('/interview_call', {
            templateUrl: recruitmentTemplatePath + 'tpl_interview_call.html',
            controller: 'InterviewCallController'
        })
        .when('/profile_recruitment', {
            templateUrl: recruitmentTemplatePath + 'tpl_profile_recruitment.html',
            controller: 'ProfileRecruitmentController'
        })
        .when('/new_assesment', {
            templateUrl: recruitmentTemplatePath + 'tpl_assesment_form.html',
            controller: 'AssesmentController'
        })
        .when('/applicant_score', {
            templateUrl: recruitmentTemplatePath + 'tpl_applicant_score.html',
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
