AssesmentModule.controller('ApplicantScoreController', ['$scope', '$location', '$upload', '$filter', 'Svc',
	function($scope,$location,$upload,$filter,Svc){

		//$scope.setLoadingTemplate(false);
		$scope.contentsLoaded = false;
		$scope.PageData 	 = {};
		$scope.date 		 = currDate;
		$scope.selectDate    = currDate;
		$scope.format 		 = 'yyyy-MM-dd';

		$scope.listOfManagements = heads;
		$scope.listOfOfficers = officers;
		$scope.listOfAllStates = allStates;

		$scope.listOfCities  = {};
		$scope.listOfDepartments  = {};
		$scope.listOfDesignations = {};
		$scope.listOfProjects = projects;
		$scope.listOfJobRecruitments = states;

		$scope.listOfEducations = {};
		$scope.listOfOrintations = {};

		$scope.existing_employee = false;
		$scope.existing_employee_department = false;
		$scope.existing_employee_designation = false;
		$scope.existing_employee_job_category = false;

		$scope.roleIDGlobal  = userRoleID;
		$scope.companyIDGlobal= userCompanyID;
		$scope.myRoleN		 = userRole;

		$scope.selectedCompanyID     = userCompanyID;
		$scope.selectedCompanyName   = userCompany;

		$scope.showCompany    = false;

		$scope.scoreModel = [];
		$scope.searchNumber ='';

		$scope.npsCall = [];
		$scope.npsCallGroup = [];

		$scope.selectedGender =0;
		$scope.selectedCS=2;
		$scope.sortObj = {
			sortby: 'name',
			sortdr: 'Asc'
		};
		$scope.page = 1;
		$scope.PagingHeaders = {};

		//$scope.setPageNameData('Recruitment');
		$scope.paramsRecruitments = {
			action: 'getRecruitmentReportData.json',
			company_id: $scope.selectedCompanyID,
		};
		/////////////////////////////////////////////////////////////////
		///////////////////////////////////////////////////////////////
		////////////////////////////////////////////////////////////////
		$scope.selectAction = function() {
			filSel = $filter('filter')($scope.listOfAllStates, {'id': $scope.applicantInformation.sub_state_id});
			$scope.applicantInformation.state = filSel[0].name.toLowerCase();
		};
		$scope.dateOptions = {
		//    dateDisabled: disabled,
		    formatYear: 'yy',
		    maxDate: new Date(),
		    minDate: new Date(2007, 1, 1),
		    startingDay: 1
		};
		$scope.dateOptionsSchedule = {
		//    dateDisabled: disabled,
		    formatYear: 'yy',
		    // maxDate: new Date(),
		    minDate: new Date(),
		    startingDay: 1
		};
		function disabled(data) {
		    var date = data.date,  mode = data.mode;
		    return mode === 'day' && (date.getDay() === 0 || date.getDay() === 6);
		 }
		$scope.from = function() {
		    $scope.popup.from = true;
	    };
	    $scope.to = function() {
		    $scope.popup.to = true;
	    };
	    $scope.schedule = function() {
		    $scope.popup.schedule = true;
	    };

		$scope.setDate = function(year, month, day) {
		    $scope.applicant.dob = new Date(year, month, day);
		};
		// $scope.popup.schedule
		$scope.popup = {
		    opened: false,
			schedule:false,

		};
		$scope.applicant = {
			id:'',
			cnic:'',
			first_name:'',
			contact:'',
			eaddress:'',
			gender:'',
			dob:new Date(),
			city:0,
			department_id:0,
			designation_id:0,
			project_id:0,
			address:'',
			employee_educations:[],
			employee_experiences:[],
			employee_orientations:[],
			employee_comments:[],

		};

		$scope.scheduler = {
			applicant_id:0,
			schedule_on:'',
			schedule_with:''
		}
		$scope.applicantInformation = {
			action: 'applicant_score', //'search_today_applicant',
			officer:"",
			state:"hired",
			sub_state_id:291,
			project_id:"",
			approved_by:"",
			from:new Date().toISOString(), //moment().format('yyyy-MM-dd'),
			to:new Date().toISOString()
		};
		$scope.showTableData = [];
		$scope.searchApplicant = function(){
			console.log($scope.applicantInformation);

			$scope.applicantInformation.from = moment($scope.applicantInformation.from).format('yyyy-MM-DD');
			$scope.applicantInformation.to = moment($scope.applicantInformation.to).format('yyyy-MM-DD');
			DashboardHelper.showLoader();
			Svc.get(
				AppCore.parseNGAjaxReq($scope.applicantInformation),
				function(response) {
					// console.log(response)
					if (response){
						//$scope.parseRecruitmentData(response);
						$scope.showTableData = response.applicant;
						DashboardHelper.hideLoader();

					}else{
						DashboardHelper.hideLoader();
						//$scope.passwordMessage = response.data.description;
					}
				},
				function(error) {
					DashboardHelper.hideLoader();
					console.log(error);
					return false;
				}
			);
		}
		$scope.searchApplicant();
		$scope.closeScheduleModel = function() {
			$('#scheduleModal').modal('hide')
		};
		$scope.openScheduleModel = function(key) {
			$scope.scheduler = {
				applicant_id:key.id,
				schedule_on:'',
				schedule_with:''
			}
			// $scope.user = key;
			// console.log($scope.user);
			// if(angular.equals({}, $scope.items)){
			// 	$scope.updateUsr 	= false;
			// 	$scope.modelName 	= "Add Schedule";
			// }
			// else{
			// 	$scope.updateUsr = true;
			// 	$scope.modelName = "Update Schedule";
			// }
			$('#scheduleModal').modal('show');

		}
		$scope.saveSchedule = function(scheduler){
			// console.log(whattodo);
			// console.log(doit);
			// $scope.applicant.employee_orientations = $scope.listOfOrintations;
			console.log($scope.scheduler);
			//console.log($scope.selectedCategory.length);

			/*var params = {
				action      : 'setEmployeeRecruitment.json',
				applicant   : JSON.stringify($scope.applicant)
			};*/
			//DashboardHelper.showLoader();
			//console.log(params);
			$scope.scheduler.schedule_on = moment($scope.scheduler.schedule_on).format('yyyy-MM-DD');
			Svc.save(
				AppCore.parseNGAjaxReq({action: 'set_scheduler'}),
			    JSON.stringify($scope.scheduler),
				function(response) {
					$scope.processSaveResponse(response);
				},
				function(error) {
					$scope.processSaveResponse(error.data);
				}
			);


			return;

			DashboardHelper.showLoader();
		};
		$scope.processSaveResponse = function(response) {
			if (response.success_status){
				$scope.closeScheduleModel();
				DashboardHelper.hideLoader();
			//	$scope.closeUserModel();
			//	$scope.getPageData();
			}else{
				//$scope.passwordMessage = response.data.description;
			}

		};
		$scope.downloadApplicant = function(){
			console.log($scope.applicantInformation);

			 ($('<form/>', {
                'id':       'tmpPDFForm',
                'action':   "../excel/downloadRecruitmentReport.json",
                'method':   'get',
                'target': '_blank'
            }).append($('<input />', { 'type': 'hidden', 'name': 'officer',  'value': $scope.applicantInformation.officer })
            ).append($('<input />', {  'type': 'hidden', 'name': 'status',    'value': $scope.applicantInformation.status })
            ).append($('<input />', {  'type': 'hidden', 'name': 'project_id',    'value': $scope.applicantInformation.project_id })
            ).append($('<input />', {  'type': 'hidden', 'name': 'approved_by',    'value': $scope.applicantInformation.approved_by })
            ).append($('<input />', {  'type': 'hidden', 'name': 'from',    'value': $scope.applicantInformation.from.toJSON().slice(0,10) })
            ).append($('<input />', {  'type': 'hidden', 'name': 'to',    'value': $scope.applicantInformation.to.toJSON().slice(0,10) })
            )).appendTo('body');
            $('form#tmpPDFForm').submit().remove();
		}


		$scope.education = {
			education_id:0,
			year:0,
			institute:''
		};
		$scope.allEdu = [];//{};
		$scope.allExperience = [];//{};

		$scope.selectedItem="";
		$scope.forwordHide= true;
		$scope.getPageData = function(params) {
			//DashboardHelper.showLoader();
			Svc.get(
				AppCore.parseNGAjaxReq(params),
				function(response) {
					if (response.data.success_status){
						$scope.parseRecruitmentData(response);
						DashboardHelper.hideLoader();

					}else{
						DashboardHelper.hideLoader();
						//$scope.passwordMessage = response.data.description;
					}
				},
				function(error) {
					console.log(error);
					return false;
				}
			);
		};
		//$scope.getPageData($scope.paramsRecruitments);
		//$scope.selectedCategory = [$scope.categories[0]];
		$scope.ValidatePhone = function(e){
			var charCode = (e.which) ? e.which : e.keyCode;
            // Allow: backspace, delete, tab, escape, enter and .
            if ($.inArray(charCode, [46, 8, 9, 27, 13, 110, 190]) !== -1 ||
                 // Allow: Ctrl+A, Command+A
                (charCode == 65 && ( e.ctrlKey === true || e.metaKey === true ) ) ||
                 // Allow: home, end, left, right, down, up
                (charCode >= 35 && charCode <= 40)) {
                     // let it happen, don't do anything
                     return;
            }
             var len = $scope.searchNumber.trim().toString().length;
            // Ensure that it is a number and stop the keypress
            if (len > 10 || (e.shiftKey || (charCode < 48 || charCode > 57))) {
                e.preventDefault();
            }

    	}

	}
]);