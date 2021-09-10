RecruitmentModule.controller('RecruitmentController', ['$scope', '$location', '$upload', '$filter', 'Svc',
	function($scope,$location,$upload,$filter,Svc){
		//return;
        //$scope.setLoadingTemplate(false);
		$scope.showTabsInView = false;
		$scope.activeTabIndex = 0;
		$scope.applicantSelectedTab = 1;

		$scope.template = {
            recruitment_form:  recruitmentTemplatePath+'tpl_recruitment_form.html',
            recruitment_queue:  recruitmentTemplatePath+'tpl_recruitment_today_queue.html',
			recruitment_employee:  recruitmentTemplatePath+'tpl_recruitment_emplyee.html',
        };
		$scope.contentsLoaded = false;
		$scope.PageData 	 = {};
		$scope.date 		 = currDate;
		$scope.selectDate    = currDate;
		$scope.format 		 = 'yyyy-MM-dd';

		$scope.employmentHistory =[];

        $scope.showTodayApplicantList = [];

        $scope.buildTree = function (elements, parentId) {
			// var _self = this;
			// console.log(elements)
			var branch = [];
			var parents = $filter('filter')(elements , {parent_id: parentId});
			// console.log(parents)
			if (parents.length > 0) {
				angular.forEach(parents, function(item, key) {
				  	children = $scope.buildTree(elements, item.id);
					if (children){ //!angular.equals({}, children)) {
						branch.push({
							id: item.id,
							group: item.group,
							name: item.name,
							slug: item.slug,
							parent_id: item.parent_id,
							status: 0,
							active: item.active,
							children: children
						});
					} else {
						branch.push({
							id: item.id,
							group: item.group,
							name: item.name,
							slug: item.slug,
							parent_id: item.parent_id,
							status: 0,
							active: item.active,
						});
					}
				}, branch);
				// parents.forEach(function (item, index, enumerable) {
				// 	children = $scope.buildTree(elements, item.get('id'));
				// 	if (!Em.isEmpty(children)) {
				// 		branch.push({
				// 			id: item.get('id'),
				// 			link: item.get('link'),
				// 			module_id: item.get('module_id'),
				// 			name: item.get('name'),
				// 			children: children
				// 		});
				// 	} else {
				// 		branch.push({
				// 			id: item.get('id'),
				// 			link: item.get('link'),
				// 			module_id: item.get('module_id'),
				// 			name: item.get('name')
				// 		});
				// 	}
				// });

			} else {
				branch = parents;
			}
			return branch;
		};
        // var departments  = {{departments|safe}};
    	// var designations  = {{designations|safe}};
    	// var projects  = {{projects|safe}};
    	// var majors  = {{majors|safe}};
    	// var institutes  = {{institutes|safe}};
    	// var educations  = {{educations|safe}};
    	// var cities  = {{cities|safe}};
    	// var languages  = {{languages|safe}};
		$scope.allfields = true;
        $scope.typing = role;
        if($scope.typing=='officer'){
        	$scope.allfields = false;
		}

		console.log($scope.typing);
        // ng-if="checked"
		$scope.listOfCities  = cities;
		$scope.listOfLangauges  = languages;
		$scope.listOfDepartments  = departments;
		$scope.listOfDesignations = designations;
		$scope.listOfProject = projects;
		$scope.listOfEducations = educations;
		$scope.listOfInstitutes = institutes;
		$scope.listOfMajors = majors;
		$scope.listOfOrintations = $scope.buildTree(orientations, '2500');
		$scope.listOfStatus = states;
		$scope.listOfRejectionReason = [{id:'', name:'Over Confidence'},
										{id:'Accent_r_sound', name:'Accent `R` Sound'},
										{id:'poor_communication_-_tp', name:'Poor Communication - TP'},

										{id:'not_confident', name:'Not Confident'},
										{id:'over_age', name:'Over Age'},
										{id:'appearance_&_body_language', name:'Appearance & Body Language'},

										{id:'not_needy', name:'Not Needy'},
										{id:'not_customer_service_profile', name:'Not Customer Service Profile'},
										{id:'not_qualified_education', name:'Not Qualified (Education)'},

										{id:'integerity_&_attitude', name:'Integerity & Attitude'},
										{id:'non_serious', name:'Non Serious'},
										{id:'not_flexible', name:'Not Flexible'},

										{id:'timing_issue', name:'Timing Issue'},
										{id:'poor_communication_-_careem', name:'Poor Communication - Careem'}];

		$scope.listOfShortlistedFor = [{id:'selected_for_tp', name:'Selected for TP'},
							   {id:'selected_for_careem', name:'Selected for Careem'},
			                   {id:'selected_for_special_projects', name:'Selected for Special Projects'},
			                   {id:'selected_for_antler', name:'Selected for Antlere'}];

		// $scope.listOfStatus = [{id:'selected_for_tp', name:'Selected for TP'},
		// 					   {id:'selected_for_careem', name:'Selected for Careem'},
		// 	                   {id:'selected_for_special_projects', name:'Selected for Special Projects'},
		// 	                   {id:'selected_for_antler', name:'Selected for Antlere'}];

















		console.log($scope.listOfOrintations);
		// $scope.listOfOrintations = angular.copy(response.data.orintations);
		// $scope.applicant.applicant_orientations = angular.copy(response.data.orintations);

		$scope.roleIDGlobal  = userRoleID;
		$scope.companyIDGlobal= userCompanyID;
		$scope.myRoleN		 = userRole;

		$scope.selectedCompanyID     = userCompanyID;
		$scope.selectedCompanyName   = userCompany;

		$scope.years = [];

		$scope.rSelect = true;
		$scope.rReject = true;

		var d = new Date();
		var n = d.getFullYear();
		$scope.years.push({id:1111, name:'Continue...'});
		for(var i=0; i<70; i++){
			$scope.years.push({id:n-i, name:n-i});
		}


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
			action: 'getRecruitmentData.json',
			company_id: $scope.selectedCompanyID,
		};
		$scope.dateOptions = {
		//    dateDisabled: disabled,
		    formatYear: 'yy',
		    maxDate: new Date(),
		    minDate: new Date(1901, 1, 1),
		    startingDay: 1
		};
		$scope.addAlert = function(type,message,time) {
		    $scope.alerts.push({ type: type, message: message, time:time});
		};

		$scope.closeAlert = function(index) {
		    $scope.alerts.splice(index, 1);
		};
		function disabled(data) {
		    var date = data.date,
		      mode = data.mode;
		    return mode === 'day' && (date.getDay() === 0 || date.getDay() === 6);
		}
		$scope.open1 = function () {
            $scope.popup.opened1 = true;
        };
		$scope.open = function() {
		    $scope.popup.opened = true;
	    };
        $scope.openStart = function (key) {
            ///console.log(key)
            $scope.popup.openedStart[key] = {
                opened: true
            };
        };
        $scope.openEnd = function (key) {
            /// console.log(key)
            $scope.popup.openedEnd[key] = {
                opened: true
            };
        };
		$scope.setDate = function(year, month, day) {
		    $scope.applicant.dob = new Date(year, month, day);
		};
		$scope.setCnicIssurenceDate = function (year, month, day) {
            $scope.applicant.cnic_insurance_date = new Date(year, month, day);
        };
		$scope.popup = {
			opened1: false,
            opened: false,
            openedStart: [],
            openedEnd: []
		};
		$scope.selectAction = function() {
			filSel = $filter('filter')($scope.listOfStatus, {'id': $scope.applicant.sub_state_id});
			$scope.applicant.state_name = filSel[0].name.toLowerCase();

		};
		$scope.cancelForm = function(){

			//$scope.listOfStatus = [{id:'', name:'Select an action'}, {id:'rejected', name:'Rejected'}, {id:'selected', name:'Selected'}];

			$scope.alerts = [];

			$scope.existing_employee = true;
			$scope.existing_applicant_department = true;
			$scope.existing_applicant_designation = true;
			$scope.existing_applicant_project = true;

			$scope.hired = false;
			$scope.message = false;
			$scope.applicant = {
				id: '',
                cnic: '', //'11111-1111111-1',
                first_name: '',
                last_name: '',
                father_name: '',
                contact: '',
                eaddress: '',
                gender: '',
                dob: new Date(1985, 05, 28),
                cnic_insurance_date: new Date(2020, 05, 28),
                city_id: '',
                department_id: '',
				desiganation_id: '',
				project_id: '',
                address: '',
                state_name: '',
				sub_state_id:'288',
                comments: '',
                source: '',
                imageText:'',
				typing:$scope.typing,
                applicant_orientations: $scope.buildTree(orientations, '2500'),
				applicant_educations: [],
                applicant_refers: [],
                applicant_experiences: [],
                applicant_typing: [],

			};
			$scope.education = {
				education_id: 0,
                year: 0,
                institute: '',
                institute_id: 0,
                major_id: 0,
                others: ''
			};
		};
		$scope.cancelForm();

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
			$scope.applicant.applicant_educations.push({
                education_id: 0,
                year: 2018,
                institute: '',
                institute_id: '',
                major_id: '',
                status: false,
                others: ''
            });
		}
		$scope.removeEducation = function(key){
			//var index = $scope.allEdu.indexOf(key);
			//if (index > -1) {
			    $scope.applicant.applicant_educations.splice(key, 1);
			//}
		}
		$scope.addExperience = function(){
			$scope.applicant.applicant_experiences.push({
                company_name: '',
                designation: '',
                job_description: '',
                started: '',
                ended: ''
            });
		}
		$scope.removeExperience = function(key){
			//var index = $scope.allEdu.indexOf(key);
			//if (index > -1) {
			    $scope.applicant.applicant_experiences.splice(key, 1);
			//}
		}
		$scope.getPageData = function(params) {
			//DashboardHelper.showLoader();
			Svc.get(
				AppCore.parseNGAjaxReq(params),
				function(response) {
                    console.log(response);
					if (response.data.success_status){
						$scope.parseRecruitmentData(response);
						DashboardHelper.hideLoader();

					}else{
						DashboardHelper.hideLoader();//$scope.passwordMessage = response.data.description;
					}
				},
				function(error) {
					console.log(error);
					return false;
				}
			);
		};
		$scope.parseRecruitmentData = function(response) {
            console.log(response);

			// $scope.listOfCities  = angular.copy(response.data.cities);
			// $scope.listOfDepartments  = angular.copy(response.data.department);
			// $scope.listOfDesignations = angular.copy(response.data.designations);
			// $scope.listOfProject = angular.copy(response.data.projects);
			// $scope.listOfEducations = angular.copy(response.data.educations);
			// $scope.listOfInstitutes = angular.copy(response.data.institutes);

			//$scope.listOfRejectionReason = angular.copy(response.data.rejection_reason);
			//$scope.listOfShortlistedFor = angular.copy(response.data.shortlisted_for);

			// $scope.listOfOrintations = angular.copy(response.data.orintations);
			// $scope.applicant.applicant_orientations = angular.copy(response.data.orintations);
			// $scope.typing = angular.copy(response.data.type);
			if(response.data.type == 'Management'){
				$scope.listOfStatus.push({id:'forword', name:'Forword'});// [{id:'', name:'Select an action'}, {id:'rejected', name:'Rejected'}, {id:'selected', name:'Selected'}];
			}
			console.log(response);
			return false;
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
		// $scope.getPageData($scope.paramsRecruitments);
		// $scope.selectedCategory = [$scope.categories[0]];
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
             var len = $scope.searchNumber.toString().length;
            // Ensure that it is a number and stop the keypress
            if (len > 10 || (e.shiftKey || (charCode < 48 || charCode > 57))) {
                e.preventDefault();
            }

    	};
		$scope.searchApplicantCnicState = function(cnic){
			$scope.applicant.cnic = cnic;
			$scope.activeTabIndex = 0.0;
			// $scope.applicantSelectedTab=0;
			// active
			$scope.searchApplicantCnic();
			// if($scope.applicant.cnic != '' || $scope.applicant.cnic > 0){
			// }; // return;
    	};
    	$scope.searchApplicantCnicBlur = function(){
    		if($scope.applicant.cnic != '' || $scope.applicant.cnic > 0){
    			$scope.searchApplicantCnic();
    		};
    		return;
    	};
		$scope.searchApplicantCnic = function(){
			console.log($scope.applicant.cnic);
            if (typeof $scope.applicant.cnic === 'undefined' || $scope.applicant.cnic == '' || $scope.applicant.cnic == 0 || $scope.applicant.cnic.length < 13){
                //alert("Enter CNIC number to test");
                warning = "Enter Complete CNIC";
                $scope.addAlert('warning', warning, '3000');
                return;
			}
			console.log($scope.applicant);

			//return;
			DashboardHelper.showLoader();
			Svc.save(
				AppCore.parseNGAjaxReq({action: 'search_applicant'}),
			    JSON.stringify({cnicNumber: $scope.applicant.cnic, form:'recruitment'}),
				function (response) {
                    console.log(response);
                    if (response.success_status) {
                        $scope.parseCnicData(response);
                    } else {
                        //$scope.setFormDefault();
                        DashboardHelper.hideLoader();
                        $scope.applicant.cnic = params.cnicNumber;
                    }
                },
                function (error) {
                    console.log(error);
                }
			);
			// var params = {
			// 		action:'searchApplicantCnic.json',
			// 		cnicNumber: $scope.applicant.cnic,
			// 		company_id: $scope.selectedCompanyID,
			// 	};
			// Svc.get(
			// 	AppCore.parseNGAjaxReq(params),
			// 	function(response) {
			// 		console.log(response);
			// 		if(response.data.success_status){
			// 			$scope.parseCnicData(response.data);
			// 		}
			// 		else{
			// 			$scope.cancelForm();
			// 			$scope.applicant.cnic = params.cnicNumber;
			// 			$scope.existing_applicant_department = true;
			// 			$scope.existing_applicant_designation = true;
			// 			$scope.existing_applicant_project = true;
			//
			// 			$scope.creator =  'Applicant not found.';
			// 			$scope.addAlert('warning',$scope.creator,'5000');
			//
			// 			DashboardHelper.hideLoader();
			// 		}
			// 	},
			// 	function(error) {
			// 		$scope.addAlert('error',error,'5000');
			// 		DashboardHelper.hideLoader();
			// 	}
			// );

		};
		$scope.processApplicantView = function(data){
            $scope.applicant.applicant_orientations = [];

			// $scope.applicant.applicant_orientations
			// console.log('orentation start');
			// console.log(data.applicant.applicant_orientations);
			// console.log(Object.keys(data.applicant.applicant_orientations));
			// console.log(Object.keys(data.applicant.applicant_orientations).length);
			// console.log($scope.listOfOrintations);

            if(Object.keys(data.applicant.applicant_orientations).length === 0){
                //$scope.listOfOrintations = angular.copy(response.data.orintations);
                $scope.applicant.applicant_orientations = angular.copy($scope.listOfOrintations);
            }
            else{
                angular.forEach($scope.listOfOrintations, function(value, key) {
                    angular.forEach(value['children'], function(innerValue, innerkey) {
                        orient = $filter('filter')(data.applicant.applicant_orientations, {'orientation_id':innerValue.id});
                        if(orient.length > 0){
                            $scope.listOfOrintations[key].children[innerkey].status = $filter('filter')(data.applicant.applicant_orientations, {'orientation_id':innerValue.id})[0].checked==1;

                            // console.log($filter('filter')(data.applicant.applicant_orientations, {'orientation_id':innerValue.id}));
                            // console.log($filter('filter')(data.applicant.applicant_orientations, {'orientation_id':innerValue.id})[0]);
                        }
                    });
                });
                $scope.applicant.applicant_orientations = angular.copy($scope.listOfOrintations);
            }
        };
		$scope.parseCnicData = function(data){
			// console.log(data);
			// return;
			if(data.status == 500 || data == ''){
				alert('sign In again');
				$window.location.href = '/aeams/login';
				return;
			}
			DashboardHelper.hideLoader();
			//	var dt = data.applicant.dob.split('T');
			//	var dt2 = dt.split('-');
			//


			console.log(data)
            console.log($scope.applicant)
			$scope.employmentHistory = angular.copy(data.employee);
            $scope.applicant = angular.copy(data.applicant);
            $scope.applicant.comments = '';
			$scope.existing_applicant_department = false;
			$scope.existing_applicant_designation = false;
			$scope.existing_applicant_project = false;

			if($scope.applicant.department_id > 0){
				$scope.existing_applicant_department = true;
			}
			if($scope.applicant.designation_id > 0){
				$scope.existing_applicant_designation = true;
			}
			if($scope.applicant.project_id > 0){
				$scope.existing_applicant_project = true;
			}

			if(data.applicant.cnic_insurance_date){
				var cidt = data.applicant.cnic_insurance_date.split('T');
				//console.log(dt);
				var cidt2 = cidt[0].split('-');
				// console.log(cidt2);
				$scope.setCnicIssurenceDate(cidt2[0], cidt2[1]-1, cidt2[2]);
			}



			var dt = data.applicant.dob.split('T');
			//console.log(dt);
			var dt2 = dt[0].split('-');
			console.log(dt2);
			// new Date(year, month, day)
			$scope.setDate(dt2[0], dt2[1]-1, dt2[2]);
			// $scope.applicant.applicant_orientations === undefined || $scope.applicant.applicant_orientations === null ||

			if($scope.applicant.state_name != 'hired' && $scope.applicant.state_name != 'shortlisted' && $scope.applicant.state_name != 'rejected' && $scope.applicant.state_name != 'selected' && $scope.applicant.state_name != 'applicant'){
				$scope.hired = false;
				$scope.message = true;
				$scope.creator =  'He is '+data.applicant.state_name+'.';
				$scope.addAlert('warning',$scope.creator,'5000');
				return;
			}
			else if(data.applicant.state_name == 'rejected' && $scope.typing == 'officer'){
				$scope.hired = true;
				$scope.message = false;
				$scope.creator =  'Applicant is '+data.applicant.state_name+' once, do you want to hire for an other project.';
				$scope.addAlert('warning',$scope.creator,'5000');
				$scope.processApplicantView(data);
				//$scope.alerts.push({ type: 'success', message: 'Applicant is '+data.applicant.state_name+'.', time:'2000'});
			}
			else if(data.applicant.state_name == 'hired' || data.applicant.state_name == 'rejected'){
				$scope.hired = false;
				$scope.message = true;
				$scope.creator =  'Applicant is '+data.applicant.state_name+'.';
				$scope.addAlert('success',$scope.creator,'5000');
				//$scope.alerts.push({ type: 'success', message: 'Applicant is '+data.applicant.state_name+'.', time:'2000'});
			}
			else if((data.applicant.state_name == 'selected' && $scope.typing == 'manager') || (data.applicant.state_name == 'shortlisted' && $scope.typing == 'officer')){ // && 'officer'
				$scope.hired   = false;
				$scope.message = true;
				$scope.creator =  'Applicant selected for Next interview. Please schedual his/her interview';
				$scope.addAlert('success',$scope.creator,'5000');
				//$scope.creator =  'Selected for second interview';
				//$scope.alerts.push({ type: '', message: '<b>Selected for second interview.</b>', time:'2000'});
				return;
			}
			else{
				$scope.message = false;
                $scope.hired = true;
            	$scope.processApplicantView(data);
            	// console.log('orentation End');
            }
            angular.forEach($scope.applicant.applicant_educations, function(value, key) {
                $scope.applicant.applicant_educations[key].others = { id:value.institute_id, name:value.institut};
            });
			angular.forEach($scope.applicant.applicant_experiences, function(value, key) {

			    var started = value.started.split('T');
			    var started = started[0].split('-');
			    var endeded = value.ended.split('T');
			    var endeded = endeded[0].split('-');

                $scope.applicant.applicant_experiences[key].started = new Date(started[0], started[1]-1, started[2]) ;
                $scope.applicant.applicant_experiences[key].ended = new Date(endeded[0], endeded[1]-1, endeded[2]) ;
            });
            // $scope.applicant.state_name += ' On Date: '+$scope.applicant.modified;


			//console.log(dt);

			// console.log(dt2);
			// new Date(year, month, day)
            $scope.applicant.typing = $scope.typing;


		//	$scope.message = false;
		//	$scope.hired = true;
		// $scope.applicant.applicant_orientations
		// console.log(Object.keys($scope.applicant.applicant_orientations).length);
		// 	console.log($scope.listOfOrintations);
		// 	if(Object.keys($scope.applicant.applicant_orientations).length === 0){
		// 		//$scope.listOfOrintations = angular.copy(response.data.orintations);
		// 		$scope.applicant.applicant_orientations = angular.copy($scope.listOfOrintations);
		// 	}
		// 	else{
		// 		angular.forEach($scope.listOfOrintations, function(value, key) {
		// 		 	//console.log(value);
		// 		 	//console.log($filter('filter')($scope.applicant.applicant_orientations, {'orientation_id':value.id})[0].status );
		// 		 	$scope.listOfOrintations[key].status = $filter('filter')($scope.applicant.applicant_orientations, {'orientation_id':value.id})[0].status;

		// 		 	angular.forEach(value['children'], function(innerValue, innerkey) {
		// 		  		$scope.listOfOrintations[key].children[innerkey].status = $filter('filter')($scope.applicant.applicant_orientations, {'orientation_id':innerValue.id})[0].status;
		// 		 	});
		// 		});
		// 		$scope.applicant.applicant_orientations = angular.copy($scope.listOfOrintations);
		// 	}
			//

			//	$scope.setDate(dt2[0], dt2[1], dt2[2]);
			//	$scope.setDate(data.applicant.dob);
			// 	$scope.npsCallGroup = angular.copy(data.npsCallGroup);
		};
		$scope.saveEmployeeInformation = function(whattodo){
            console.log("Imin save Employee");
			console.log(whattodo);
			// if($scope.applicant.state_name == ""){//!$scope.recruitmentForm.comments.$valid){
			// 	alert("Select employee Coments.");
			// 	return false;
			// }
			// if( $scope.applicant.state_name <= 1 ){ //!$scope.recruitmentForm.state_name.$valid){//} == '' || $scope.applicant.state_name <= 1 ){
			// 	alert("Select applicant state.");
			// 	return false;
			// }
			// if (!$scope.recruitmentForm.$valid) {
			// 	return false;
			// 	//alert('our form is amazing');
			// }
			// console.log(doit);
			// $scope.applicant.applicant_orientations = $scope.listOfOrintations;
			// console.log($scope.applicant); return false;
			// console.log($scope.selectedCategory.length);
			/*
			var params = { action:'setEmployeeRecruitment.json', applicant:JSON.stringify($scope.applicant)};
			*/
			angular.forEach($scope.applicant.applicant_educations, function (value, key) {
                var insti = value.others;
                $scope.applicant.applicant_educations[key].institute_id = insti.id;
                $scope.applicant.applicant_educations[key].institute = insti.name;
            });
			$scope.applicant.cnic_insurance_date = moment($scope.applicant.cnic_insurance_date).format('yyyy-MM-DD');
            $scope.applicant.dob = moment($scope.applicant.dob).format('yyyy-MM-DD');
			angular.forEach($scope.applicant.applicant_experiences, function (value, key) {
                $scope.applicant.applicant_experiences[key].started = moment(value.started).format('yyyy-MM-DD');
                $scope.applicant.applicant_experiences[key].ended = moment(value.ended).format('yyyy-MM-DD');
            });
			DashboardHelper.showLoader();
			// console.log(params);
			Svc.save(
				AppCore.parseNGAjaxReq({action: 'applicant_assesment'}),
			    JSON.stringify($scope.applicant),
				function(response) {
					$scope.processSaveResponse(response);
				},
				function(error) {
					$scope.processSaveResponse(error.data);
				}
			);

			return;
		};
		$scope.processSaveResponse = function(response) {
			console.log(response)
			if (response.success_status){
				$scope.addAlert('success','Saved successfully','5000');
				DashboardHelper.hideLoader();
				$scope.cancelForm();
				//  DashboardHelper.hideLoader();
				//	$scope.closeUserModel();
				//	$scope.getPageData();
			}else{
				$scope.addAlert('success',response.data,'5000');
				//$scope.passwordMessage = response.data.description;
			}

		};
		$scope.closeUserModel = function() {
			$('#userAddModal').modal('hide')
        };
        $scope.loadTodayApplicantList = function(tfor){
            console.log('imin')
            DashboardHelper.showLoader();
            // 'searchTodayApplicantList.json',
            if($scope.typing== 'manager' && tfor == 'applicant'){
				tfor = 'shortlisted';
			}else if($scope.typing== 'head' && tfor == 'applicant'){
				tfor = 'selected';
			}
			else if($scope.typing== 'officer' && tfor == 'selected'){
				tfor = 'shortlisted';
			}else if($scope.typing== 'head' && tfor == 'selected'){
				tfor = 'hired';
			// }else{
			//
			}
            var params = {
                action: 'search_today_applicant',
                form:$scope.typing,
                state:tfor,
                from:moment().format('yyyy-MM-DD'),
				to:moment().format('yyyy-MM-DD')
			};
            Svc.get(
                AppCore.parseNGAjaxReq(params),
                function (response) {
                    console.log(response);
                    if (response.success_status) {
                        //$scope.parseCnicData(response.data);
                        $scope.showTodayApplicantList = angular.copy(response.applicant);
                        DashboardHelper.hideLoader();
                    }
                },
                function (error) {
                    $scope.addAlert('error', error, '5000');
                    DashboardHelper.hideLoader();
                }
            );
        };
		$scope.openUserModel = function(key) {$scope.processSaveResponse
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
        $scope.refreshResults = function($select){
            var search = $select.search,
            list = angular.copy($select.items),
            FLAG = -1;
            //remove last user input
            list = list.filter(function(item) {
                return item.id !== FLAG;
            });

            if (!search) {
              //use the predefined list
                $select.items = list;
            }
            else {
              //manually add user input and set selection
                var userInputItem = {
                    id: FLAG,
                    name: search
                };
                $select.items = [userInputItem].concat(list);
                $select.selected = userInputItem;
            }
        };

    }
]);
