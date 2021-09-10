var DashboardHelper = {
    showLoader: function () {
        AppCore.loader.show({
            text: 'Working'
        });
    },
    hideLoader: function () {
        AppCore.loader.hide();
    },
    isEmptyObjMem: function (mem) {
        if (angular.isUndefined(mem) || !mem || mem == null || mem == '') {
            return true;
        }
        return false;
    }
};
var LoginLocation = '';
var RecruitmentModule = angular.module('Recruitment', ['ngRoute', 'ngAnimate', 'ngResource', 'ngMessages', 'ui.bootstrap', 'AppFilter', 'AppDirective', 'ui.select', 'angularFileUpload', 'ngSanitize', 'ngCookies', 'treeGrid', 'ui.mask']).run( function run( $http, $cookies ){
    // For CSRF token compatibility with Django
    $http.defaults.headers.post['X-CSRFToken'] = $cookies.get('csrftoken');
});
RecruitmentModule.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);



/*function AdminCtrl($scope,$location,SvcAdmin) {

	$scope.loginErrFlg = false;
	$scope.loginErrMsg = null;
	$scope.logingUser = false;
	$scope.btnGrey = true;
	$scope.btnGreen = false;

	$scope.errorEmailEmpty = true;
	$scope.step_1 = true;

	$scope.errorMsgEmail = null;
	$scope.errorEmailEmpty = false;
	$scope.errorEmail = false;
	$scope.email = '';

	$scope.applyEvents = function() {
		$('#UserUsername, #UserPassword')
		.keyup(function(e) {
			if (e.keyCode == 13) {
				$scope.$apply($scope.doLogin());
			}
		});
		$('#inputEmail').blur(function() {
			var email = $('#inputEmail').val();
			if (email=="") {
				$scope.errorEmailEmpty = true;

			}else{
				$scope.errorEmailEmpty = false;
			}
		});
	};

	$scope.applyEvents();
	$scope.isFormValid = function() {
		return true;
	};

	$scope.doLoginData = null;
	$scope.doLogin = function() {
		if ($scope.logingUser) {
			return;
		}
		if (!$scope.isFormValid()) {
			return;
		}
		var postData = $('#UserLoginForm').serialize();
		$scope.logingUser = true;
		AppCore.loader.show({text: 'Loading'});
		SvcLogin.save(
			AppCore.parseNGAjaxReq({}),
			AppCore.serializeReqData(postData),
			function(response) {
//				console.log(response); return;
				$scope.loginErrFlg = false;
				AppCore.loader.hide();
				AppCore.webService.response = response;
				if (AppCore.webService.isResponseSuccess()) {
					$scope.doLoginData = response.data.data;
					$scope.doLoginParseData();
				} else {
					$scope.logingUser = false;
					var error_desc = response.data.description;
					$scope.loginErrFlg = true;
					$scope.loginErrMsg = error_desc;
				}
			}
		);
	};
	$scope.doLoginParseData = function() {
		if (typeof $scope.doLoginData.secret_question_undefined !== 'undefined' && $scope.doLoginData.secret_question_undefined) {
			$scope.logingUser = false;
			//$("#securityQAModal").modal();
			AppCore.redirect($scope.doLoginData.next_url);
		} else {
			AppCore.redirect($scope.doLoginData.next_url);
		}
	};
	$scope.securityQACancel = function() {
		AppCore.redirect($scope.doLoginData.next_url);
	};
	$scope.securityQASubmit = function() {
		AppCore.redirect($scope.doLoginData.secret_question_url);
	};

	$scope.validateForgetPassWord = function() {

		$scope.errorEmailEmpty = false;
		$scope.errorEmail = false;
		var reg = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
		if ($scope.email == ''){
			$scope.errorEmailEmpty = true;
			$scope.errorEmail = true;
			$scope.btnGreen = false;
			$scope.btnGrey = true;
			$scope.errorMsgEmail = "Please provide email address";
			return false;
		}else if (reg.test($scope.email) == false){
			$scope.errorEmailEmpty = true;
			$scope.errorEmail = true;
			$scope.btnGrey = true;
			$scope.btnGreen = false;
			$scope.errorMsgEmail = "Invalid email address";
			return false;
		}else{
			$scope.btnGrey = false;
			$scope.btnGreen = true;
			return true;
		}
	}

	$scope.forgetPassWord = function() {

		if ($scope.validateForgetPassWord() == false){
			return false;
		}
		var postData = $('#UserForgotPasswordForm').serialize();
		AppCore.loader.show({text: 'Loading'});
		SvcForgotPassword.save(
			AppCore.parseNGAjaxReq({}),
			AppCore.serializeReqData(postData),
			function(response) {
				AppCore.loader.hide();
				if (response.data.success_status == 1) {
					$("#forgotPanel").html($("#forgetSuccessMsg").html());
				} else {
					$scope.errorEmailEmpty = true;
					$scope.errorEmail = true;
					$scope.errorMsgEmail = response.data.description;
				}
			}
		);
	};
}
function QuestionCtrl($scope,$routeParams, $location, SvcValidatePasswordRequest, SvcValidateQuestion, SaveNewPassword, SvcCheckAnswer) {
	$scope.btnGrey = true;
	$scope.btnGreen = false;
	$scope.user_detail = [];

	$scope.secret_question = '';
	$scope.secret_answer = '';

	$scope.divQuestion = true;
	$scope.divNewPassword = false;

	$scope.new_password = '';
	$scope.re_new_password = '';
	$scope.errorNewPassword = null;
	$scope.errorReNewPassword = null;
	$scope.errorMsgNewPassword = '';
	$scope.errorMsgReNewPassword = '';
	$scope.errorMsgAnswer = '';
	$scope.errorAnswerFlg = null;
	$scope.passwordMessage = '';
	$scope.user_id = 0;
	$scope.ServiceInProgress = false;

	$scope.btnLogin = false;
	$scope.errorMsgPassword = 'Please provide a new password.';

	$scope.getPageData = function() {
		var params = {
			action: 'getLibraryLandingPage',
			hash: $routeParams.hash,
		};
		SvcValidatePasswordRequest.get(
			AppCore.parseNGAjaxReq(params),
			function(response) {
				if (response.data.success_status){
					$scope.user_detail = response.data.data.UserDetail;
					$scope.secret_question = $scope.user_detail.secret_question;
					$scope.user_id = $scope.user_detail.user_id;
					$scope.passwordMessage = '';
				}else{
					$scope.passwordMessage = response.data.description;
				}
			},
			function(error) {
				console.log(error);
				return false;
			}
		);
	};
	$scope.getPageData();
	$scope.validateAnswer = function() {
		if ($scope.secret_answer == ''){
			$scope.errorMsgAnswer = 'Please type answer';
			$scope.errorAnswerFlg = false;
			$scope.btnGrey = true;
			$scope.btnGreen = false;
			return false;
		}else{
			$scope.errorMsgAnswer = '';
			$scope.btnGrey = false;
			$scope.btnGreen = true;
			$scope.errorAnswerFlg = true;
			return true;
		}
	}

	$scope.submitAnswer = function() {
		if ($scope.ServiceInProgress == true){
			alert('Password Checking is already in Progress');
			return false;
		}else if ($scope.validateAnswer()){
			AppCore.loader.show({text: 'Loading'});
			var postData = $('#frmSecurityQuestion').serialize();
			$scope.ServiceInProgress = true;
			SvcCheckAnswer.save(
				AppCore.parseNGAjaxReq({}),
				AppCore.serializeReqData(postData),
				function(response) {
					console.log(response);
					AppCore.loader.hide();
				//	$scope.passwordMessage = response.data.description;	;
					$scope.ServiceInProgress = false;
					if (response.data.success_status == 1) {

						var user_id = $scope.user_id;
						$scope.divQuestion = false;
						$scope.divNewPassword = true;
						$scope.btnGrey = true;
						$scope.btnGreen = false;
						$scope.btnLogin = true;
					}else{
						$scope.errorMsgAnswer = response.data.description;
						$scope.errorAnswerFlg = false;
						$scope.btnGrey = true;
						$scope.btnGreen = false;
						return false;
					}
				}
			);
		}else{
			return false;
		}
	};

	$scope.checkValidNewPassword = function() {

		var newPassword = $scope.new_password;
		$scope.errorMsgNewPassword = '';
		$scope.btnGrey = true;
		$scope.btnGreen = false;
		if ((newPassword.length <= 12) && (newPassword.length >= 8)){
			$scope.errorNewPassword = true;
			return true;
		}else if (newPassword.length == 0){
			$scope.errorMsgNewPassword = 'Password may not be empty';
			$scope.errorNewPassword = false;
			return false;
		}else if (newPassword.length < 8){
			$scope.errorNewPassword = false;
			$scope.errorMsgNewPassword = 'Minimum 8 alphanumeric characters ';
			return false;
		}else if (newPassword.length > 12){
			$scope.errorMsgNewPassword = 'Maximum 12 alphanumeric characters ';
			$scope.errorNewPassword = false;
			return false;
		}
	}

	$scope.checkValidReNewPassword = function() {

		var newPassword = $scope.new_password;
		var reNewPassword = $scope.re_new_password;
		$scope.btnGrey = true;
		$scope.btnGreen = false;
		$scope.errorMsgReNewPassword = '';
		if (newPassword == reNewPassword){
			$scope.errorReNewPassword = true;
			$scope.btnGrey = false;
			$scope.btnGreen = true;
			return true;
		}else if ((newPassword != reNewPassword) && (reNewPassword.length >= 8)){
			$scope.errorReNewPassword = false;
			$scope.errorMsgReNewPassword = 'Password confirm does not match!';
			return false;
		}
	}

	$scope.saveNewPassword = function() {
		if (!($scope.checkValidNewPassword()))
			return false;
		if (!($scope.checkValidReNewPassword()))
			return false;

		AppCore.loader.show({text: 'Loading'});
		var postData = $('#frmNewPassword').serialize();
		SaveNewPassword.save(
			AppCore.parseNGAjaxReq({}),
			AppCore.serializeReqData(postData),
			function(response) {
				AppCore.loader.hide();
				$scope.passwordMessage = response.data.description;	;
				if (response.data.success_status == 1) {
					$scope.btnLogin = true;
				}
			}
		);
	};
}
*/
