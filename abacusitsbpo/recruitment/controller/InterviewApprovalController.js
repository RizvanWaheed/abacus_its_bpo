RecruitmentModule.controller('InterviewApprovalController', ['$scope', '$location', '$upload', '$filter', 'Svc',
	function($scope,$location,$upload,$filter,Svc){

		//$scope.setLoadingTemplate(false);
		$scope.contentsLoaded = false;
		$scope.PageData 	 = {};
		$scope.date 		 = currDate;
		$scope.selectDate    = currDate;
		$scope.format 		 = 'yyyy-MM-dd';

		$scope.listOfManagements = heads;
		$scope.listOfOfficers = officers;

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
		$scope.dateOptions = {
		//    dateDisabled: disabled,
		    formatYear: 'yy',
		    maxDate: new Date(),
		    minDate: new Date(2007, 1, 1),
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

		$scope.setDate = function(year, month, day) {
		    $scope.applicant.dob = new Date(year, month, day);
		};

		$scope.popup = {
		    opened: false
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
		$scope.applicantInformation = {
			action: 'getRecruitmentReport.json',
			officer:"0",
			status:"0",
			project_id:"0",
			approved_by:"0",
			from:new Date(), //moment().format('yyyy-MM-dd'),
			to:new Date()
		};
		$scope.showTableData = [];
		$scope.searchApplicant = function(){
			console.log($scope.applicantInformation);
			DashboardHelper.showLoader();
			Svc.get(
				AppCore.parseNGAjaxReq($scope.applicantInformation),
				function(response) {
					if (response.data.success_status){
						//$scope.parseRecruitmentData(response);
						$scope.showTableData = response.data.recruitment;
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
		$scope.updateselectedItem=function(){
			//alert($scope.selectedItem);
			if($scope.selectedItem == 'Forward'){
				$scope.forwordHide= false;
			}else{
				$scope.forwordHide= true;
			}
		}
		/*$scope.updateselectedItem = function(){
			$scope.allEdu.push({ education_id:0, year:0, institute:'' });
		}*/


		$scope.addEducation = function(){
			$scope.applicant.employee_educations.push({ education_id:0, year:0, institute:'' });
		}
		$scope.removeEducation = function(key){
			//console.log(key);
			//console.log($scope.allEdu);

			//var index = $scope.allEdu.indexOf(key);
			//console.log(index);
			//if (index > -1) {
		    $scope.applicant.employee_educations.splice(key, 1);
			//}
		}
		$scope.addExperience = function(){
			$scope.applicant.employee_experiences.push({ company_name:'', designation:'', job_description:'', started:'', ended:''});
		}
		$scope.removeExperience = function(key){
			//console.log(key);
			//console.log($scope.allEdu);

			//var index = $scope.allEdu.indexOf(key);
			//console.log(index);
			//if (index > -1) {
			 $scope.applicant.employee_experiences.splice(key, 1);
			//}
		}
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
		$scope.parseRecruitmentData = function(response) {


			$scope.listOfOfficers  = angular.copy(response.data.officers);
			$scope.listOfManagements  = angular.copy(response.data.managements);
			// $scope.listOfProjects = angular.copy(response.data.projects);
			$scope.listOfJobRecruitments = angular.copy(response.data.recruitments);
			//$scope.listOfEducations = angular.copy(response.data.educations);
			//$scope.listOfOrintations = angular.copy(response.data.orintations);
			//$scope.applicant.employee_orientations = angular.copy(response.data.orintations);
			//console.log(response);
			//return;
			/*console.log($scope.companies[0].categories_levels);

			$scope.callStatus	= angular.copy(response.data.call_status);
			$scope.categories	= angular.copy(response.data.categories);
			$scope.categories_levels = $scope.companies[0].categories_levels;
			$scope.affinityList = [];
			for(var i = 1; i<= $scope.categories_levels; i++){
				console.log(i);
				$scope.affinityList.push({
					headLine   : 'Affinity Level '+i,
					categoryID : 'AffinityID'+i,
					categoryLevel : i,
					categoryData : [],
				});
			}


			$scope.parseSelectedAffinityData(0, 0);

			$scope.gender	 	= angular.copy(response.data.gender);
			$scope.selectedCategory = [$scope.categories[0]];*/

		};
		$scope.parseSelectedAffinityData = function(level, category_id) {
			console.log(level);
			console.log($scope.categories_levels);
			//return false;
			if($scope.categories_levels == level){
				$scope.selectedCategory = category_id;
				return true;
			}
			var newLevel = level+1;
			$scope.affinityList[level].categoryData = [];
			angular.forEach($scope.categories, function(value, key) {
				if(value.level == newLevel && value.category_id == category_id){
					$scope.affinityList[level].categoryData.push($scope.categories[key]);
				}

			});
			//console.log($scope.affinityList[0].categoryData);
		}
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
		$scope.searchApplicantCnic = function(){
			//console.log($scope.searchNumber);
			if($scope.applicant.cnic.trim() == ''){
				alert("Enter CNIC number to test");
				return;
			}
			console.log($scope.applicant);

			//return;
			DashboardHelper.showLoader();
			var params = {
					action:'searchApplicantCnic.json',
					cnicNumber: $scope.applicant.cnic.trim(),
					company_id: $scope.selectedCompanyID,
				};
			Svc.get(
				AppCore.parseNGAjaxReq(params),
				function(response) {
					console.log(response);
					if(response.data.success_status){
						$scope.parseCnicData(response.data);
					}
					else{
						DashboardHelper.hideLoader();
					}
				},
				function(error) {
					console.log(error);

				}
			);

		};
		$scope.parseCnicData = function(data){
			console.log(data);
			// return;
			if(data.status == 500 || data == ''){
				alert('sign In again');
				$window.location.href = 'http://localhost:1234/cem';
				return;
			}
			DashboardHelper.hideLoader();
		//	var dt = data.applicant[0].dob.split('T');
		//	var dt2 = dt.split('-');
			//
			$scope.applicant = angular.copy(data.applicant[0]);
			//$scope.applicant.employee_orientations === undefined || $scope.applicant.employee_orientations === null ||
			if(Object.keys($scope.applicant.employee_orientations).length === 0){
				//$scope.listOfOrintations = angular.copy(response.data.orintations);
				$scope.applicant.employee_orientations = angular.copy($scope.listOfOrintations);
			}
			else{
				angular.forEach($scope.listOfOrintations, function(value, key) {
				 	console.log(value);
				 	console.log($filter('filter')($scope.applicant.employee_orientations, {'orientation_id':value.id})[0].status );
				 	$scope.listOfOrintations[key].status = $filter('filter')($scope.applicant.employee_orientations, {'orientation_id':value.id})[0].status;

				 	angular.forEach(value['children'], function(innerValue, innerkey) {
				  		$scope.listOfOrintations[key].children[innerkey].status = $filter('filter')($scope.applicant.employee_orientations, {'orientation_id':innerValue.id})[0].status;
				 	});
				});
				$scope.applicant.employee_orientations = angular.copy($scope.listOfOrintations);
			}
			$scope.existing_employee_department = false;
			$scope.existing_employee_designation = false;
			$scope.existing_employee_project = false;
			if($scope.applicant.department_id > 0){
				$scope.existing_employee_department = true;
			}
			if($scope.applicant.designation_id > 0){
				$scope.existing_employee_designation = true;
			}
			if($scope.applicant.job_category_id > 0){
				$scope.existing_employee_job_category = true;
			}
			var dt = data.applicant[0].dob.split('T');
			//console.log(dt);
			var dt2 = dt[0].split('-');
			console.log(dt2);
			$scope.setDate(dt2[0], dt2[1]-1, dt2[2]);//

//	$scope.setDate(dt2[0], dt2[1], dt2[2]);




			//$scope.setDate(data.applicant[0].dob);
			// $scope.npsCallGroup = angular.copy(data.npsCallGroup);
		};
		$scope.saveEmployeeInformation = function(whattodo){
			console.log(whattodo);
			// console.log(doit);
			// $scope.applicant.employee_orientations = $scope.listOfOrintations;
			console.log($scope.applicant);
			//console.log($scope.selectedCategory.length);

			/*var params = {
				action      : 'setEmployeeRecruitment.json',
				applicant   : JSON.stringify($scope.applicant)
			};*/
			//DashboardHelper.showLoader();
			//console.log(params);
			Svc.save(
				AppCore.parseNGAjaxReq({action: 'setCandidate.json'}),
			    JSON.stringify($scope.applicant),
				function(response) {
					$scope.processSaveResponse(response);
				},
				function(error) {
					$scope.processSaveResponse(error.data);
				}
			);


			return;
			console.log(listOfOrintations);
			if(typeof $scope.npsCall.id !== 'undefined'){
				if($scope.npsCall.id < 0){
					alert("No customer found");
				    return;
				}
			}
			if(typeof $scope.npsCall.id === 'undefined'){
				alert("No customer found");
			    return;
			}
			if($scope.searchNumber.trim() == ''){
				alert("Enter the Phone number...");
				return;
			}
			if($scope.selectedCategory.length < 1){
				alert("Select a Category...");
				return false;
			}
			if($scope.selectedGender == ""){
				alert("Select Gender ...");
				return false;
			}
			if($scope.scoreModel == ""){
				alert("Select Score ...");
				return false;
			}
			if($scope.feedbackMod == ""){
				alert("Enter Feedback ...");
				return false;
			}
			if($scope.selectedCS == ""){
				alert("Select a Call Status ...");
				return false;
			}
			var params = {
				action      :'setActivities.json',
				gender   	: $scope.selectedGender,
				category_id : JSON.stringify($scope.selectedCategory),
				score       : $scope.scoreModel,
				score_reason: $scope.feedbackMod,
				call_status : $scope.selectedCS,
				customer_id : $scope.npsCall.id,
				company_id:$scope.selectedCompanyID
			}
			DashboardHelper.showLoader();
			console.log(params);
			Svc.get(
				AppCore.parseNGAjaxReq(params),
				function(response) {
					$scope.processSaveResponse(response);
				},
				function(error) {
					$scope.processSaveResponse(error.data);
				}
			);

		};
		$scope.processSaveResponse = function(response) {
			if (response.data.success_status){
				DashboardHelper.hideLoader();
			//	$scope.closeUserModel();
			//	$scope.getPageData();
			}else{
				//$scope.passwordMessage = response.data.description;
			}

		};
		$scope.closeUserModel = function() {
			$('#userAddModal').modal('hide')
		};
		$scope.openUserModel = function(key) {


			if(key != '' || key == '0'){
				keyVal = parseInt(key);
				//console.log($scope.users[keyVal].user_id);
				$scope.updateUsersVal = $scope.users[keyVal];//angular.copy();
				$scope.updateUsr = true;
				$scope.modelName = "Update User";
				$scope.selectedRole = $scope.updateUsersVal.role_id;
				$scope.showUserReportingTo(keyVal);
				$scope.selectedReporting = $scope.users[keyVal].user_id;
			}
			else{
				$scope.updateUsr 	= false;
				$scope.modelName 	= "Add User";
				$scope.selectedRole = 0;
				$scope.updateUsersVal ={
					id:0,
					username:'',
					password:'',
				}
			//	$scope.selectedRole = "";
				$scope.selectedReporting = 0;
			}
			//console.log($scope.updateUsersVal);
			$('#userAddModal').modal();
		};

	}
]);