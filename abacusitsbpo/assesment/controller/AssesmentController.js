AssesmentModule.controller('AssesmentController', ['$scope', '$location', '$upload', '$filter', 'Svc',
	function($scope,$location,$upload,$filter,Svc){
		//return;
        //$scope.setLoadingTemplate(false);
		$scope.showTabsInView = false;
		$scope.activeTabIndex = 0;
		$scope.applicantSelectedTab = 1;

		// $scope.template = {
        //     recruitment_form:  recruitmentTemplatePath+'tpl_recruitment_form.html',
        //     recruitment_queue:  recruitmentTemplatePath+'tpl_recruitment_today_queue.html'
        // };
		$scope.contentsLoaded = false;
		$scope.PageData 	 = {};
		$scope.date 		 = currDate;
		$scope.selectDate    = currDate;
		$scope.format 		 = 'yyyy-MM-dd';

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
				form:'assesment',
				id: '',
                cnic: '', //'11111-1111111-1',
                first_name: '',
                last_name: '',
                father_name: '',
                contact: '',
                eaddress: '',
                gender: '',
                dob: new Date(1985, 05, 28),
                cnic_insurance_date: new Date(1985, 05, 28),
                city_id: '',
                department_id: '',
				desiganation_id: '',
				project_id: '',
                address: '',
                state_name: '',
				sub_state_id:'',
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
		$scope.getPageData = function() {
			//DashboardHelper.showLoader();
			Svc.get(
				AppCore.parseNGAjaxReq({action:'get_orientation', typing:$scope.typing}),
				function(response) {
                    console.log(response);
					if (response.success_status){
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
		$scope.getPageData();
		$scope.parseRecruitmentData = function(response) {
            console.log(response);

            $scope.listOfOrintations = $scope.buildTree(response.orientations, '2500');
            $scope.applicant.applicant_orientations = angular.copy($scope.listOfOrintations);
            return;
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
			lastCnicNumber = $scope.applicant.cnic;
			DashboardHelper.showLoader();
			Svc.save(
				AppCore.parseNGAjaxReq({action: 'search_applicant'}),
			    JSON.stringify({cnicNumber: $scope.applicant.cnic, form:'assesment'}),
				function (response) {
                    console.log(response);
                    if (response.success_status) {
                        $scope.parseCnicData(response);
                    } else {
                        DashboardHelper.hideLoader(); //$scope.setFormDefault();
                        $scope.applicant.cnic = lastCnicNumber;
                    }
                },
                function (error) {
                    console.log(error);
                }
			);
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
                    // console.log(value);
                    // console.log($filter('filter')($scope.applicant.applicant_orientations, {'orientation_id':value.id})[0].status );
                    // $scope.listOfOrintations[key].status = $filter('filter')($scope.applicant.applicant_orientations, {'orientation_id':value.id})[0].status;

                    angular.forEach(value['children'], function(innerValue, innerkey) {
                        // console.log($filter('filter')(data.applicant.applicant_orientations, {'orientation_id':innerValue.id}));
                        orient = $filter('filter')(data.applicant.applicant_orientations, {'orientation_id':innerValue.id});
                        if(orient.length > 0){
                            // console.log($filter('filter')(data.applicant.applicant_orientations, {'orientation_id':innerValue.id}));
                            $scope.listOfOrintations[key].children[innerkey].status = $filter('filter')(data.applicant.applicant_orientations, {'orientation_id':innerValue.id})[0].checked==1;
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

			console.log(data)
            console.log($scope.applicant)

            $scope.applicant = angular.copy(data.applicant);
			$scope.processApplicantView(data);

            $scope.applicant.typing = $scope.typing;
		};
		$scope.saveOrientation = function(){
			DashboardHelper.showLoader();
			// console.log(params);
			Svc.save(
				AppCore.parseNGAjaxReq({action: 'set_orientation'}),
			    JSON.stringify($scope.applicant),
				function(response) {
					$scope.processSaveResponse(response);
				},
				function(error) {
					$scope.processSaveResponse(error.data);
				}
			);
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
